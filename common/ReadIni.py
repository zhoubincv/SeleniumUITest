from configparser import ConfigParser
import ProjectDirPath


class ReadIni:
    def __init__(self):
        self.config_reader = ConfigParser()

    def get_config_file(self) -> ConfigParser:
        file_name = ProjectDirPath.project_path + "/RegisterConfig.ini"
        config_file = self.config_reader
        config_file.read(file_name)
        return config_file


if __name__ == '__main__':
    pass
