import json
import os
import pygit2
import re
import sys
from time import gmtime, strftime

with open('config.json') as config_file:
    config = json.load(config_file)

global repo_name
global repo
global commit_start
global commit_end

output_folder = 'output/'


def commit_filter(commit):
    rule = r'{0}'.format(config['commit_rule'])
    if re.search(rule, commit.message) is not None:
        return True
    else:
        return False


def extract_commit(message):
    rule = r'{0}'.format(config['commit_rule'])
    return re.search(rule, message).group()


def init(repo_location, start, end):
    global repo_name
    global commit_start
    global commit_end
    global repo

    repo_name = repo_location
    repo = pygit2.Repository(repo_name)

    commit_end = repo.revparse_single(end)
    commit_start = repo.revparse_single(start)


def extract_commit_info(commit, full):
    if full:
        commit_formatted = commit.hex + ':' +commit.author.name + ' - [' + commit.author.email + ']@' + str(commit.author.time)
        commit_formatted += commit.hex + ' - ' + commit.message
    else:
        commit_formatted = commit.hex + ' - ' + commit.message

    return commit_formatted


def generate_release():
    global commit_start
    global commit_end
    global repo

    commit_list = []

    repo = pygit2.Repository(repo_name)

    history_filename = output_folder + 'history' + '.txt'
    ff = open(history_filename, 'w', encoding='utf8')

    ff.write('Full History \n')

    for commit in repo.walk(commit_start.hex, pygit2.GIT_SORT_TOPOLOGICAL):
        if commit.hex != commit_end.hex:
            ff.write(extract_commit_info(commit, True))
            if commit_filter(commit):
                filtered_commit = extract_commit(commit.message)
                if not (filtered_commit in commit_list):
                    commit_list.append(filtered_commit)
        else:
            break
    return commit_list


def check_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def generate(start_release, end_release):
    check_exists(output_folder)
    init(config['repo_path'], end_release, start_release)

    relase_file_name = output_folder + 'release_' + end_release + '.txt'
    f = open(relase_file_name, 'w', encoding='utf8')
    f.write('Release ' + end_release + '\n')
    f.write('\n')
    f.write(strftime('Generated %a, %d %b %Y %H:%M:%S \n', gmtime()))
    f.write('\n')

    for trello in generate_release():
        f.write(trello + '\n')

    f.close()
    config_file.close()


def main(argv):

    if len(argv) >= 2:
        generate(argv[0], argv[1])
    else:
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
