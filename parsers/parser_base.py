#!/usr/bin/env python
from pathlib import Path        # allows OS independent pathing
import json
import datetime
import os


class ReportParser:
    def __init__(self, source_directory, output_directory):
        self.source_directory = source_directory
        self.output_directory = output_directory
        self.file_pattern = "*"
        self.service = "unknown"

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

    def build_output_file_name(self, output_report):
        report_date = output_report["report_date"]
        return "{0}_{1}.json".format(report_date, self.service)

    def get_all_reports(self):
        ReportParser.info("Parsing reports at: {0}".format(self.source_directory.absolute()))

        files_in_report = ReportParser.get_files_by_pattern(self.source_directory, self.file_pattern)
        if not files_in_report or len(files_in_report) == 0:
            ReportParser.error("No report files found in {0}".format(self.source_directory))

        return files_in_report

    def write_report(self, json_report, output_file):
        try:
            output_path = Path(os.path.dirname(__file__))
            output_path = Path.joinpath(output_path, self.output_directory)

            # TODO: Add security checks around this?
            Path(output_path).mkdir(parents=True, exist_ok=True)

            file_path = Path.joinpath(output_path, output_file)
            ReportParser.info("Writing report to {0}/{1}".format(file_path, output_file))


            # TODO: Add security checks around this?
            with open(file_path, 'w') as fh:
                json.dump(json_report, fh)
            return output_path
        except IOError:
            ReportParser.error("Unable to write report at {0}".format(file_path))
        return None