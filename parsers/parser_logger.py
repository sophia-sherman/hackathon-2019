import logging
import os
import datetime
from pathlib import Path


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ParserLogger(metaclass=Singleton):
    def __init__(self):
        self.log_file_root = "parser_log"
        self.output_directory = "output_reports/"
        self.output_file = self.prepare_log_file()
        logging.basicConfig(filename=self.output_file,level=logging.INFO)
        print("Log files will be displayed at {0}".format(self.output_file))

    def info(self, data):
        logging.info(data)

    def error(self, data):
        logging.error(data)

    def prepare_log_file(self):
        output_path = Path(os.path.dirname(__file__))
        output_path = Path.joinpath(output_path, self.output_directory)

        # TODO: Add security checks around this?
        Path(output_path).mkdir(parents=True, exist_ok=True)

        output_file = self.log_file_root + ParserLogger.get_current_timestamp() + ".log"
        file_path = Path.joinpath(output_path, output_file)
        return file_path

    @staticmethod
    def get_current_timestamp():
        datetime_object = datetime.datetime.now()
        formated_data = datetime_object.strftime("%Y%m%d_%H%M%S")
        return formated_data
