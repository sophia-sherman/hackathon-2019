#!/usr/bin/env python
from pathlib import Path        # allows OS independent pathing
import json
import os
from parsers.parser_helpers import ParserHelpers
from parsers.parser_extractors import ReportExtractors
import datetime
import dateutil.relativedelta


class ReportParser:
    def __init__(self, source_directory, output_directory):
        self.source_directory = source_directory
        self.output_directory = output_directory
        self.service = "unknown"
        self.coverage_type = "unknown"

    # INTAKE

    @staticmethod
    def get_files_by_pattern(path, pattern):
        assert isinstance(path, Path)
        return list(path.glob(pattern))

    def get_all_reports(self, file_pattern):
        ParserHelpers.info("Parsing reports at: {0}".format(self.source_directory.absolute()))

        files_in_report = ReportParser.get_files_by_pattern(self.source_directory, file_pattern)
        files_in_report = ReportParser.keep_reports_by_time_block(file_list=files_in_report, months_to_keep=2)

        if not files_in_report or len(files_in_report) == 0:
            ParserHelpers.error("No report files found in {0}".format(self.source_directory))

        return files_in_report

    @staticmethod
    def keep_reports_by_time_block(file_list, months_to_keep):
        trimmed_list = []
        current_datetime = datetime.datetime.now()
        earliest_date = current_datetime - dateutil.relativedelta.relativedelta(months=months_to_keep)

        for file in file_list:
            file_date = ParserHelpers.extract_date_from_filename(source_file=file)
            if earliest_date <= file_date <= current_datetime:
                trimmed_list.append(file)
        return trimmed_list

    # OUTPUT

    def build_output_file_name(self, output_report, coverage_type):
        report_date = output_report["report_date"]
        return "{0}_{1}_{2}.json".format(report_date, self.service, coverage_type)

    def build_report(self, report_history, coverage_type):
        json_report = {}
        json_report["service"] = self.service
        json_report["report_date"] = ParserHelpers.get_current_timestamp()
        json_report["coverage_type"] = coverage_type
        json_report["report_history"] = report_history
        return json_report

    def write_report(self, json_report, output_report, coverage_type):
        output_file = self.build_output_file_name(output_report=output_report, coverage_type=coverage_type)
        file_path = ""

        try:
            output_path = Path(os.path.dirname(__file__))
            output_path = Path.joinpath(output_path, self.output_directory)

            # TODO: Add security checks around this?
            Path(output_path).mkdir(parents=True, exist_ok=True)

            file_path = Path.joinpath(output_path, output_file)
            ParserHelpers.info("Writing report to {0}/{1}".format(file_path, output_file))


            # TODO: Add security checks around this?
            with open(file_path, 'w') as fh:
                json.dump(json_report, fh)
            return file_path
        except IOError:
            ParserHelpers.error("Unable to write report at {0}".format(file_path))
        return None

    # GENERATORS

    def parse_reports(self):
        report_outputs = []

        for coverage_type in self.coverage_type:
            if coverage_type == "cloverage":
                file_pattern = "*-cloverage.html"
                report_files = self.get_all_reports(file_pattern=file_pattern)
                report_output = self.cloverage_generate_reports(report_files=report_files, coverage_type=coverage_type)
                if report_output:
                    report_outputs.append(report_output)
            elif coverage_type == "jest":
                file_pattern = "*-jest.txt"
                report_files = self.get_all_reports(file_pattern=file_pattern)
                report_output = self.jest_generate_reports(report_files=report_files, coverage_type=coverage_type)
                if report_output:
                    report_outputs.append(report_output)
            elif coverage_type == "gatling":
                file_pattern = "*-gatling.out"
                report_files = self.get_all_reports(file_pattern=file_pattern)
                report_output = self.gatling_generate_reports(report_files=report_files, coverage_type=coverage_type)
                if report_output:
                    report_outputs.append(report_output)

        return report_outputs

    def jest_generate_reports(self, report_files, coverage_type):
        report_history = ReportExtractors.jest_extract_reports(report_files=report_files)
        output_report = self.build_report(report_history=report_history, coverage_type=coverage_type)
        return self.write_report(json_report=output_report, output_report=output_report, coverage_type=coverage_type)

    def cloverage_generate_reports(self, report_files, coverage_type):
        report_history = ReportExtractors.cloverage_extract_reports(report_files)
        output_report = self.build_report(report_history=report_history, coverage_type=coverage_type)
        return self.write_report(json_report=output_report, output_report=output_report, coverage_type=coverage_type)

    def gatling_generate_reports(self, report_files, coverage_type):
        report_history = ReportExtractors.gatling_extract_reports(report_files)
        output_report = self.build_report(report_history=report_history, coverage_type=coverage_type)
        return self.write_report(json_report=output_report, output_report=output_report, coverage_type=coverage_type)
