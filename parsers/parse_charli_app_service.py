#!/usr/bin/env python
from pathlib import Path
from parsers.parser_base import ReportParser
from bs4 import BeautifulSoup   # HTML Parsing


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
        report_files = self.get_all_reports()
        report_history = []

        for file in report_files:
            print("{0}".format(file))
            value = ReportParserCAS.extract_field(file_path=file)
            if value:
                json_data = ReportParserCAS.format_report_field(source_file=file, form_total=value)
                report_history.append(json_data)

        output_report =  self.build_report(report_history=report_history)
        output_file = self.build_output_file_name(output_report=output_report)
        return self.write_report(json_report=output_report, output_file=output_file)

    def build_report(self, report_history):
        json_report = {}
        json_report["service"] = self.service
        json_report["report_date"] = ReportParser.get_timestamp()
        json_report["coverage_type"] = self.coverage_type
        json_report["report_history"] = report_history
        return json_report

    @staticmethod
    def format_report_field(source_file, form_total):
        json_data = {}
        json_data['source_file'] = source_file.name
        json_data['source_date'] = ReportParser.extract_date_from_filename(source_file)
        try:
            json_data['stmts'] = ReportParserCAS.format_value_to_float(form_total)
        except ValueError:
            ReportParser.error("Unable to convert {0} to float, setting to -1".format(stmts))
            json_data['form_total'] = -1
        return json_data

    @staticmethod
    def format_value_to_float(value):
        # current format: 47.95 %
        extracted_value = value.split(' ')
        try:
            new_value = float(extracted_value[0])
            return new_value
        except ValueError:
            ReportParser.error("Unable to extract float from: {0}".format(value))
        except IndexError:
            ReportParser.error("Unable to extract float from: {0}".format(value))
        return -1

    @staticmethod
    def extract_field(file_path):
        tr_field = "Totals:"
        td_class = "with-number"
        td_index = 0       # 0 is Forms, 1 is Lines

        try:
            with open(file_path,'r') as fh:
                soup = BeautifulSoup(fh, "html.parser")
                trs = soup.find_all('tr')
                for tr in trs:
                    tds = tr.find_all('td')
                    for td in tds:
                        if td.text == "Totals:":
                            return list(tr.find_all('td', {"class": td_class}))[td_index].text
            ReportParser.error("Field <{0}><{1}> not found in file {2}".format(tr_field, td_class, file_path))
        except IOError:
            ReportParser.error("Unable to open report at {0}".format(file_path))
        except IndexError:
            ReportParser.error("File {0} was not formatted as expected, field not found".format(file_path))
        return None
