from flask import Flask, escape, request

app = Flask(__name__)

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
                    {
                        "service": "charlie-app-mobile",
                        "report_date": "20191106_112411",
                        "coverage_type": "jest",
                        "report_history": [
                            {
                            "source_file": "20191106_091711-jest.txt",
                            "source_date": "20191106_091711",
                            "stmts": "44.45"
                            },
                            {
                            "source_file": "20191105_081711-jest.txt",
                            "source_date": "20191105_081711",
                            "stmts": "33.29"
                            }
                        ]
                    }
                )
            return measures
        else:
            return 'No project keys submitted', 200
    else:
        return 'No project keys submitted', 200
