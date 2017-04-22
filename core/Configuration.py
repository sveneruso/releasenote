import json


class Configuration(object):

    def __init__(self, configuration_file=None):

        if configuration_file is None:
            configuration_file = 'config.json'

        with open(configuration_file) as self.config_file:
            config = json.load(self.config_file)

        self.config = config

    def commit_rule(self):
        return self.config['commit_rule']

    def commit_match_group(self):
        if 'commit_match_group' in self.config:
            group = self.config['commit_match_group']
        else:
            group = 0

        return group

    def repo_path(self):
        return self.config['repo_path']

    def output_folder(self):
        return self.config['output_folder']

    def close_config_file(self):
        self.config_file.close()
