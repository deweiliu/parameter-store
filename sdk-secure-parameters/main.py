import json
from flatten_json import flatten_json
from put_parameter import put_parameter
import apps

# This directory is in .gitignore
params_dir = '../secure-parameters/'

# Get all app names
app_names = apps.get(params_dir)

# For each app
for app_name in app_names.keys():

    # Load secure parameters
    with open(app_names[app_name], 'r') as f:
        json_params = json.loads(f.read())

    # Restructure the JSON object
    params = flatten_json(json_params, app_name)

    # For each parameter
    for key in params.keys():
        # Create secure parameter in SSM Parameter Store
        put_parameter(key, params[key])
