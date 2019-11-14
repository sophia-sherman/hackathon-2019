#!/usr/bin/env python
from pathlib import Path
from parsers.parser_base import ReportParser
from parsers.parser_extractors import ReportExtractors


class ReportParserCAS(ReportParser):
    def __init__(self, source_directory, output_directory):
        ReportParser.__init__(self, source_directory, output_directory)
        self.service = "charli-app-service"
        self.file_pattern = "*-cloverage.html"
        self.coverage_type = "cloverage"

        self.source_directory = Path(source_directory)
        self.source_directory = Path.joinpath(self.source_directory, self.service)
        self.output_directory = Path(output_directory)
        self.output_directory = Path.joinpath(self.output_directory, self.service)

    def parse_reports(self):
        report_files = self.get_all_reports(file_pattern=self.file_pattern)

        report_history = ReportExtractors.cloverage_extract_reports(report_files)

        output_report =  self.build_report(report_history=report_history, coverage_type=self.coverage_type)
        output_file = self.build_output_file_name(output_report=output_report, coverage_type=self.coverage_type)
        return self.write_report(json_report=output_report, output_file=output_file)
