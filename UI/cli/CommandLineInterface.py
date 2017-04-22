from time import gmtime, strftime

from core.Configuration import Configuration
from core.FileHandler import FileHandler
from core.RepoReader import RepoReader


class CommandLineInterface(object):
    def __init__(self, start, end):
        self.configuration = Configuration()
        self.start = start
        self.end = end
        release_file_name = 'release-' + end
        self.release_file = FileHandler(self.configuration.output_folder(), release_file_name, '.txt')
        self.history_file = FileHandler(self.configuration.output_folder(), 'history', '.txt')
        self.__generate_headers()

    def __generate_headers(self):
        header = strftime('Generated %a, %d %b %Y %H:%M:%S', gmtime())
        release = '[ ' + self.start + ' - ' + self.end + ' ]'
        self.release_file.write(header)
        self.release_file.write(release)

        self.history_file.write(header)
        self.history_file.write(release)

    def release_note(self):
        repo = RepoReader(self.configuration, self.start, self.end)
        filtered, full = repo.generate_relase()

        for filtered_commit in filtered:
            self.release_file.write(filtered_commit)

        self.release_file.close()

        for full_commit in full:
            self.history_file.write(full_commit)

        self.history_file.close()
