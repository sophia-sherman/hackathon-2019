#!/usr/bin/env python
import optparse         # allows OptionParser for command line options
import sys              # allows sys.exit

from parsers.parse_charli_app_mobile import ReportParserCAM
from parsers.parse_charli_app_service import ReportParserCAS


def parse_report(service_name, source_directory="data", output_directory="output_reports"):
    print("Parsing (service) {0}, (source) {1}, (dest) {2}".format(service_name, source_directory, output_directory))

    if service_name == "charli-app-mobile":
        parser = ReportParserCAM(source_directory, output_directory)
    elif service_name == "charli-app-service":
        parser = ReportParserCAS(source_directory, output_directory)
    else:
        print ("Service {0} is not supported at this time".format(service_name))
        sys.exit(0)

    output = parser.parse_reports()
    if output:
        print("Report written to: {0}".format(output))
    else:
        print("Error: unable to write a report for {0}".format(service_name))
    return output


def parse_reports(source_directory="data", output_directory="output_reports"):
    output_paths = []
    print("Parsing all reports")

    report_path = parse_report("charli-app-mobile", source_directory, output_directory)
    if report_path:
        output_paths.append(report_path)

    print("Parsed reports complete {0}".format(output_paths))
    return output_paths


def main():
    options = parse_options()
    input_root = "data/"
    if options.input_root:
        input_root = options.input_root

    output_root = "output_reports/"
    if options.output_root:
        output_root = options.output_root
    print("(input_root) {0} (output_report) {1}".format(input_root, output_root))

    if options.service_name:
        parse_report(options.service_name, source_directory=input_root, output_directory=output_root)
    else:
        parse_reports()

    sys.exit(0)


def parse_options():
    # https://docs.python.org/2/library/optparse.html
    p = optparse.OptionParser(
        description="Parse Report",
        prog="parse_reports",
        usage="\n%prog --[service] [service name]\n"
    )
    # actions:
    #   store_true | store_false - stores a boolean value
    #   store (store a variable) as type (int | float | string)  : default is string
    #   store_const - store a constant value
    #   append - append this option's argument to a list
    #   count - increment a counter by one
    #   callback - call a specified function
    p.add_option('--service', '-s', action="store", dest="service_name", type="string",
                 help="Parse the report just for this service")
    p.add_option('--input', '-i', action="store", dest="input_root", type="string",
                 help="The root source of the reports")
    p.add_option('--output', '-o', action="store", dest="output_root", type="string",
                 help="The root source of the output")
    options, args = p.parse_args()
    return options


#   https://stackoverflow.com/questions/419163/what-does-if-name-main-do
#   if this is the directly executed module then __name__ will be set to be "__main__", else will be module name
if __name__ == "__main__":
    # execute function 'main' if we get in here (ie. run the program)
    main()
    # thene exit 0 if we haven't exited yet for whatever reason
    sys.exit(0)
