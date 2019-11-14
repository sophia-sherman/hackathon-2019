#!/usr/bin/env python
from pathlib import Path
from parsers.parser_base import ReportParser


class ReportParserCAM(ReportParser):
    def __init__(self, source_directory, output_directory):
        ReportParser.__init__(self, source_directory, output_directory)
        self.service = "charli-app-mobile"
        self.file_pattern = "*-jest.txt"
        self.coverage_type = "jest"

        self.source_directory = Path(source_directory)
        self.source_directory = Path.joinpath(self.source_directory, self.service)
        self.output_directory = Path(output_directory)
        self.output_directory = Path.joinpath(self.output_directory, self.service)

    def build_report(self, report_history):
        json_report = {}
        json_report["service"] = self.service
        json_report["report_date"] = ReportParser.get_timestamp()
        json_report["coverage_type"] = self.coverage_type
        json_report["report_history"] = report_history
        return json_report

    def parse_reports(self):
        report_files = self.get_all_reports()
        report_history = []

        for file in report_files:
            print("{0}".format(file))
            value = ReportParserCAM.jest_extract_column(file, 1)
            if value:
                json_data = ReportParser.format_report_field(source_file=file, value_display='stmts', value=value)
                report_history.append(json_data)

        output_report =  self.build_report(report_history=report_history)
        output_file = self.build_output_file_name(output_report=output_report)
        return self.write_report(json_report=output_report, output_file=output_file)


    @staticmethod
    def jest_extract_column(file_path, column_number):
        line_pattern = "All files"
        line_delim = "|"

        try:
            with open(file_path,'r') as fh:
                line = fh.readline()
                while line:
                    if line_pattern in line:
                        value = line.split(line_delim)[column_number].strip()
                        return value
                    line = fh.readline()
                ReportParser.error("Pattern {0} not found in file {1}".format(line_pattern, file_path))
        except IOError:
            ReportParser.error("Unable to open report at {0}".format(file_path))
        except IndexError:
            ReportParser.error("Unable to find column {0} in file: {1}".format(column_number, file_path))
        return None
