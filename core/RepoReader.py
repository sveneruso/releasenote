import re
import pygit2


class RepoReader(object):

    def __init__(self, config, start, end):
        self.config = config
        self.repo = pygit2.Repository(self.config.repo_path())
        self.start_commit = self.repo.revparse_single(start)
        self.end_commit = self.repo.revparse_single(end)

    def __is_valid_commit(self, commit):
        rule = r'{0}'.format(self.config.commit_rule())
        if re.search(rule, commit.message) is not None:
            return True
        else:
            return False

    def __extract_commit(self, message):
        rule = r'{0}'.format(self.config.commit_rule())
        return re.search(rule, message).group(self.config.commit_match_group())

    def __extract_commit_info(self, commit, full):
        if full:
            commit_formatted = commit.hex + ':' + commit.author.name + ' - [' + commit.author.email + ']@' + str(commit.author.time)
            commit_formatted += commit.hex + ' - ' + commit.message
        else:
            commit_formatted = commit.hex + ' - ' + commit.message

        return commit_formatted

    def generate_relase(self):
        commit_list = []
        full_commit_list = []
        for commit in self.repo.walk(self.end_commit.hex, pygit2.GIT_SORT_TOPOLOGICAL):
            if commit.hex != self.start_commit.hex:
                full_commit_list.append(self.__extract_commit_info(commit, True))
                if self.__is_valid_commit(commit):
                    filtered_commit = self.__extract_commit(commit.message)
                    if not (filtered_commit in commit_list):
                        commit_list.append(filtered_commit)
            else:
                break

        return commit_list, full_commit_list
