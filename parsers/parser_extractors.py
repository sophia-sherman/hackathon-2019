from parsers.parser_base import ReportParser
from bs4 import BeautifulSoup   # HTML Parsing


class ReportExtractors:
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
            ReportParser.error("Field <{0}><{1}> not found in file {2}".format(tr_field, td_class, file_path))
        except IOError:
            ReportParser.error("Unable to open report at {0}".format(file_path))
        except IndexError:
            ReportParser.error("File {0} was not formatted as expected, field not found".format(file_path))
        return None

    @staticmethod
    def cloverage_extract_reports(report_files):
        report_history = []

        for file in report_files:
            print("{0}".format(file))
            value = ReportExtractors.cloverage_extract_field(file_path=file)
            if value:
                numeric_value = ReportParser.format_percent_to_float(value)
                json_data = ReportParser.format_report_field(source_file=file, value_display='value',
                                                             value=numeric_value)
                report_history.append(json_data)
        return report_history

    @staticmethod
    def jest_extract_reports(report_files):
        report_history = []

        for file in report_files:
            print("{0}".format(file))
            value = ReportExtractors.jest_extract_column(file, 1)
            if value:
                json_data = ReportParser.format_report_field(source_file=file, value_display='value', value=value)
                report_history.append(json_data)
        return  report_history
