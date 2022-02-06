from put_parameter import put_parameter
from prepare_params import prepare_params

all_params = prepare_params()
# For each parameter
for key in all_params.keys():
    # Create secure parameter in SSM Parameter Store
    put_parameter(key, all_params[key])
