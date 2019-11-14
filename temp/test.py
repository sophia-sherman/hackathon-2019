import sys
sys.path.append('..')
from parsers import parse_reports

print(parse_reports.parse_reports(source_directory="../parsers/data"))