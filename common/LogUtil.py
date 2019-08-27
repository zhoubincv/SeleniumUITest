import logging
import os
import time
import ProjectDirPath

recording_time = time.localtime()
log_dir_name = time.strftime("%Y-%m", recording_time)
log_file_name = time.strftime("%Y-%m-%d", recording_time)
log_path = ProjectDirPath.project_path + "/logs/" + log_dir_name
if os.path.exists(log_path):
    pass
else:
    os.makedirs(log_path)
log_file_path = log_path + "/" + log_file_name + ".log"


class LogRecorder:
    def __init__(self):
        self.logger = logging.getLogger()
        formatter = logging.Formatter("%(asctime)s -> %(module)s -> %(funcName)s -> %(lineno)d -> %(message)s")
        self.logger.setLevel(logging.DEBUG)
        self.file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

    def get_logger(self):
        return self.logger

    def close(self):
        self.logger.removeHandler(self.file_handler)
        self.file_handler.close()


log_recorder = LogRecorder()


if __name__ == '__main__':
   pass
