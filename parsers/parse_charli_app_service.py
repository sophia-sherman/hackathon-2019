#!/usr/bin/env python
from pathlib import Path
from parsers.parser_base import ReportParser


class ReportParserCAS(ReportParser):
    def __init__(self):
        ReportParser.__init__(self)
        self.service = "charli-app-service"
        self.file_pattern = "*-cloverage.html"
        self.coverage_type = "cloverage"

        self.root_directory = Path.joinpath(self.root_directory, self.service)
        self.output_directory = Path.joinpath(self.output_directory, self.service)

