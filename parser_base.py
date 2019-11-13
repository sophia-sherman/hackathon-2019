#!/usr/bin/env python
from pathlib import Path        # allows OS independent pathing
import json
import datetime

class ReportParser:
    def __init__(self):
        self.root_directory = Path("data/")
        self.output_directory = Path("output_reports/")
        self.file_pattern = "*"

    @staticmethod
    def info(data):
        print(data)

    @staticmethod
    def error(data):
        print(data)

    def parse_reports(self):
        self.error("No reports to parse: no parser specified")

    @staticmethod
    def get_files_by_pattern(path, pattern):
        assert isinstance(path, Path)
        return list(path.glob(pattern))

    @staticmethod
    def extract_date_from_filename(source_file):
        file_stem = source_file.stem
        file_split = file_stem.split("-")
        if not file_split or len(file_split) < 1:
            return "bad_format"
        return file_split[0]

    @staticmethod
    def get_timestamp():
        datetime_object = datetime.datetime.now()
        formated_data = datetime_object.strftime("%Y%m%d_%H%M%S")
        return formated_data

    def get_all_reports(self):
        ReportParser.info("Parsing reports at: {0}".format(self.root_directory))

        files_in_report = ReportParser.get_files_by_pattern(self.root_directory, self.file_pattern)
        if not files_in_report or len(files_in_report) == 0:
            ReportParser.error("No report files found in {0}".format(self.root_directory))

        return files_in_report

    @staticmethod
    def write_report(json_report, output_path):
        try:
            ReportParser.info("Writing report to {0}".format(output_path))
            with open(output_path, 'w') as fh:
                json.dump(json_report, fh)
            return output_path
        except IOError:
            ReportParser.error("Unable to write report at {0}".format(json_report))
        return None
