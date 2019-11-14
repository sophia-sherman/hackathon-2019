import sys
sys.path.append('..')
from parsers import parse_reports

# print(parse_reports.parse_reports(source_directory="../parsers/data"))
print(parse_reports.parse_report(service_name="charli-app-service", source_directory="../parsers/data"))