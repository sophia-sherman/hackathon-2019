#!/usr/bin/env python
from pathlib import Path
from server.api.parsers.parser_base import ReportParser


class ReportParserCAS(ReportParser):
    def __init__(self):
        ReportParser.__init__(self)
        self.root_directory = Path.joinpath(self.root_directory, "charli-app-service")

    def parse_reports(self):
        ReportParser.info("Parsing reports at: {0}".format(self.root_directory))

