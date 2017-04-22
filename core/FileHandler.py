import os


class FileHandler(object):

    def __check_exists(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def __init__(self, path, file_name, extension, mode='w'):
        self.path = path
        self.complete_file_path = path + file_name + extension
        self.__check_exists()
        self.file = open(self.complete_file_path, mode, encoding='utf8')

    def write(self, text):
        self.file.write(text + '\n')

    def close(self):
        self.file.close()
