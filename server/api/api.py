from flask import Flask, escape, request

app = Flask(__name__)

projects = [
        {'name':'Journi FE', 'id':1},
        {'name':'Journi BE', 'id':2}
    ]

metrics = [
        {'name':'coverage', 'id':1},
        {'name':'performance', 'id':2}
    ]

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/projects')
def get_projects():
    return {'projects': projects}

@app.route('/metrics')
def get_metrics():
    return {'metrics': metrics}

@app.route('/metrics/<metric_id>')
def get_metrics_for_project(metric_id):
    if request.args:

        # We have our query string nicely serialized as a Python dictionary
        args = request.args

        if "project_id" in args:
            metric_dict = {x.id: x for x in metrics}
            project_dict = {x.id: x for x in projects}
            return {
                'metric': metric_dict[metric_id],
                'project': project_dict[args.get("project_id")],
                'latest_value': 30
                }
        else:
            return "No project requested", 200
    else:
        return "No query string received", 200
