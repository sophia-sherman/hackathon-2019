from flask import Flask, escape, request
from flask_cors import CORS
import json
from parsers.parse_reports import parse_report
from .measures.jira import jira_issues

app = Flask(__name__)
CORS(app)

projects = [
    {'key': 'charli-app-mobile'},
    {'key': 'charli-app-service'}
]

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/search_projects')
def get_projects():
    return {'projects': projects}

@app.route('/search')
def get_metrics():
    if request.args:
        args = request.args

        if "projectKeys" in args:
            keys = args["projectKeys"].split(" ")
            measures = {'measures': []}
            if 'charli-app-service' in keys:
                measures['measures'].append(
                    retrieve_coverage_info('charli-app-service')
                )
            if 'charli-app-mobile' in keys:
                measures['measures'].append(
                    retrieve_coverage_info('charli-app-mobile')
                )
            return measures
        else:
            return 'No project keys submitted', 200
    else:
        return 'No project keys submitted', 200

@app.route('/bugs')
def get_bugs():
    measures = {'measures': []}
    measures['measures'].append(retrieve_jira_info_for_product())
    return measures


@app.route('/performance')
def get_performance():
    if request.args:
        args = request.args

        if "projectKeys" in args:
            keys = args["projectKeys"].split(" ")
            measures = {'measures': []}
            if 'charli-app-service' in keys:
                measures['measures'].append(
                    retrieve_performance_info('charli-app-service')
                )
            return measures
        else:
            return 'No project keys submitted', 200
    else:
        return 'No project keys submitted', 200


def retrieve_coverage_info(projectKey):
    report_paths = parse_report(projectKey, source_directory="parsers/data")
    for path in report_paths:
        if ('cloverage' in path.stem) or ('jest' in path.stem):
            with open(path) as json_file:
                data = json.load(json_file)
                return data


def retrieve_performance_info(projectKey):
    report_paths = parse_report(projectKey, source_directory="parsers/data")
    for path in report_paths:
        print(path.stem)
        if 'gatling' in path.stem:
            with open(path) as json_file:
                print('Found file')
                data = json.load(json_file)
                return data


def retrieve_jira_info_for_product():
    jira = {
        'open_critical_major_bugs': jira_issues.count_open_critical_major_issues(),
        'open_data_quality_bugs': jira_issues.count_open_data_issues(),
        'open_regressions': jira_issues.count_open_regression_issues(),
        'opened_during_sprint': jira_issues.count_opened_issues_in_sprint(),
        'closed_during_sprint': jira_issues.count_closed_issues_in_sprint(),
        'total_open_bugs': jira_issues.count_open_issues()
    }
    return jira
