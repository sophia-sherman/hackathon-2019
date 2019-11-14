import datetime
import re                       # regular expressions (string parsing)


class ParserHelpers:
    @staticmethod
    def info(data):
        print(data)

    @staticmethod
    def error(data):
        print(data)

    @staticmethod
    def format_percent_to_float(value):
        # current format: 47.95 %
        extracted_value = value.split(' ')
        try:
            new_value = float(extracted_value[0])
            return new_value
        except ValueError:
            ParserHelpers.error("Unable to extract float from: {0}".format(value))
        except IndexError:
            ParserHelpers.error("Unable to extract float from: {0}".format(value))
        return -1

    @staticmethod
    def extract_date_from_filename(source_file):
        file_stem = source_file.stem
        file_split = file_stem.split("-")
        try:
            extracted_date = datetime.datetime.strptime(file_split[0], '%Y%m%d_%H%M%S')
            formated_data = extracted_date.strftime("%Y-%m-%d")
            return formated_data
        except IndexError:
            ParserHelpers.error("Unable to extract a date from filename {0}".format(source_file))
        except ValueError:
            ParserHelpers.error("Unable to extract date format from {0}".format(source_file))
        return "-1"

    @staticmethod
    def get_timestamp():
        datetime_object = datetime.datetime.now()
        formated_data = datetime_object.strftime("%Y%m%d_%H%M%S")
        return formated_data

    @staticmethod
    def safe_string_to_float(src):
        try:
            output = float(src)
            return output
        except ValueError:
            ParserHelpers.error("Unable to convert {0} to float, setting to -1.0".format(src))
        return -1.0

    @staticmethod
    def format_report_field_float(source_file, value_display, value):
        json_data = {}
        json_data['source_file'] = source_file.name
        json_data['source_date'] = ParserHelpers.extract_date_from_filename(source_file)
        json_data[value_display] = ParserHelpers.safe_string_to_float(value)
        return json_data

    @staticmethod
    def format_report_field_json(source_file, value_display, value):
        json_data = {}
        json_data['source_file'] = source_file.name
        json_data['source_date'] = ParserHelpers.extract_date_from_filename(source_file)
        json_data[value_display] = value
        return json_data

    @staticmethod
    def regex_extract_float_from_string(src_string, pattern):
        try:
            extracted_value = re.search(pattern, src_string).group(1)
            float_value = ParserHelpers.safe_string_to_float(extracted_value)
            return float_value
        except AttributeError:
            ParserHelpers.error("Unable to extract values from: {0}".format(src_string))
