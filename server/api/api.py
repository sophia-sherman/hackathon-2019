from flask import Flask, escape, request
from flask_cors import CORS
import json
from .parsers.parse_reports import parse_report
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
                    retrieve_project_info('charli-app-service')
                )
            if 'charli-app-mobile' in keys:
                measures['measures'].append(
                    retrieve_project_info('charli-app-mobile')
                )
            return measures
        else:
            return 'No project keys submitted', 200
    else:
        return 'No project keys submitted', 200


def retrieve_project_info(projectKey):
    report_path = parse_report(projectKey)
    with open(report_path) as json_file:
        data = json.load(json_file)
        return data