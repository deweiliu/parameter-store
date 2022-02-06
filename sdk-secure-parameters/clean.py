import boto3
from prepare_params import prepare_params

client = boto3.client('ssm')

defined_params = prepare_params().keys()


remote_params = client.describe_parameters(
    ParameterFilters=[
        {
            "Key": "Type",
            "Values": ["SecureString"]
        }
    ]
)['Parameters']

params = []

for parameter in remote_params:
    name = parameter['Name']
    if name not in defined_params:
        if name != '/core/mysql/user/master/password':
            params.append(name)

if(len(params) > 0):
    response = client.delete_parameters(Names=params)
    print(response)
print('Done cleaning secure params')
