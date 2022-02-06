import json
from flatten_json import flatten_json
import apps

def prepare_params():
    # This directory is in .gitignore
    params_dir = '../secure-parameters/'

    # Get all app names
    app_names = apps.get(params_dir)

    all_params = dict()
    # For each app
    for app_name in app_names.keys():

        # Load secure parameters
        with open(app_names[app_name], 'r') as f:
            json_params = json.loads(f.read())

        # Restructure the JSON object
        params = flatten_json(json_params, app_name)

        all_params = all_params | params
    return all_params