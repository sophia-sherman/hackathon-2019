#!/usr/bin/env python
from pathlib import Path
from parsers.parser_base import ReportParser


class ReportParserCAM(ReportParser):
    def __init__(self, source_directory, output_directory):
        ReportParser.__init__(self, source_directory, output_directory)
        self.service = "charli-app-mobile"
        self.coverage_type = ["jest"]

        self.source_directory = Path(source_directory)
        self.source_directory = Path.joinpath(self.source_directory, self.service)
        self.output_directory = Path(output_directory)
        self.output_directory = Path.joinpath(self.output_directory, self.service)

