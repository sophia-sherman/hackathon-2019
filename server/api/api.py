from flask import Flask, escape, request
from flask_cors import CORS
import json

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
                    {
                        "service": "charlie-app-service",
                        "report_date": "20191106_112411",
                        "coverage_type": "cloverage",
                        "report_history": [
                            {
                            "source_file": "20191106_091711-cloverage.html",
                            "source_date": "20191106_091711",
                            "stmts": "47.95"
                            },
                            {
                            "source_file": "20191105_081711-cloverage.html",
                            "source_date": "20191105_081711",
                            "stmts": "23.29"
                            }
                        ]
                    }
                )
            if 'charli-app-mobile' in keys:
                measures['measures'].append(
                    retrieve_project_info()
                )
            return measures
        else:
            return 'No project keys submitted', 200
    else:
        return 'No project keys submitted', 200


def retrieve_project_info():
    with open('../output_reports/charli-app-mobile/20191106_112411_charlie_app_mobile.json') as json_file:
        data = json.load(json_file)
        return data