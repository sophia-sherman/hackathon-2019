from parsers.parser_helpers import ParserHelpers
from bs4 import BeautifulSoup   # HTML Parsing


class ReportExtractors:
    # JEST

    @staticmethod
    def jest_extract_reports(report_files):
        report_history = []

        for file in report_files:
            ParserHelpers.info("{0}".format(file))
            value = ReportExtractors.jest_extract_column(file, 1)
            if value:
                json_data = ParserHelpers.format_report_field_float(source_file=file, value_display='value', value=value)
                report_history.append(json_data)
        return report_history

    @staticmethod
    def jest_extract_column(file_path, column_number):
        line_pattern = "All files"
        line_delim = "|"

        try:
            with open(file_path, 'r') as fh:
                line = fh.readline()
                while line:
                    if line_pattern in line:
                        value = line.split(line_delim)[column_number].strip()
                        return value
                    line = fh.readline()
                ParserHelpers.error("Pattern {0} not found in file {1}".format(line_pattern, file_path))
        except IOError:
            ParserHelpers.error("Unable to open report at {0}".format(file_path))
        except IndexError:
            ParserHelpers.error("Unable to find column {0} in file: {1}".format(column_number, file_path))
        return None

    # CLOVERAGE

    @staticmethod
    def cloverage_extract_reports(report_files):
        report_history = []

        for file in report_files:
            ParserHelpers.info("{0}".format(file))
            percent_value = ReportExtractors.cloverage_extract_field(file_path=file)
            if percent_value:
                value = ParserHelpers.format_percent_to_float(percent_value)
                json_data = ParserHelpers.format_report_field_float(source_file=file, value_display='value', value=value)
                report_history.append(json_data)
        return report_history

    @staticmethod
    def cloverage_extract_field(file_path):
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
            ParserHelpers.error("Field <{0}><{1}> not found in file {2}".format(tr_field, td_class, file_path))
        except IOError:
            ParserHelpers.error("Unable to open report at {0}".format(file_path))
        except IndexError:
            ParserHelpers.error("File {0} was not formatted as expected, field not found".format(file_path))
        return None

    # GATLING

    @staticmethod
    def gatling_extract_reports(report_files):
        report_history = []

        for file in report_files:
            ParserHelpers.info("{0}".format(file))
            request_mean = ReportExtractors.gatling_get_line(file_path=file, label="mean requests/sec")
            response_mean = ReportExtractors.gatling_get_line(file_path=file, label="mean response time")
            ko_percent = ReportExtractors.gatling_get_line(file_path=file, label="failed")

            json_value = {}
            json_value['request_mean'] = ParserHelpers.regex_extract_float_from_string(src_string=request_mean, pattern=".*?([\d\.]+)\s*\(")
            json_value['response_mean'] = ParserHelpers.regex_extract_float_from_string(src_string=response_mean, pattern=".*?([\d\.]+)\s*\(")
            json_value['ko_percent'] = ParserHelpers.regex_extract_float_from_string(src_string=ko_percent, pattern=".*?\(\s*([\d\.]+)%")

            json_data = ParserHelpers.format_report_field_json(source_file=file, value_display='value', value=json_value)

            report_history.append(json_data)
        return report_history


    @staticmethod
    def gatling_get_line(file_path, label):
        try:
            with open(file_path, 'r') as fh:
                line = fh.readline()
                while line:
                    if label in line:
                        return line
                    line = fh.readline()
                ParserHelpers.error("Label {0} not found in file {1}".format(line, file_path))
        except IOError:
            ParserHelpers.error("Unable to open report at {0}".format(file_path))
        return None
