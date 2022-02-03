import boto3

client = boto3.client('ssm')
def put_parameter(path, value):
    response = client.put_parameter(
        Name = path,
        Value = value,
        Type = 'SecureString',
        Overwrite = True,
        Tier = 'Standard',
        DataType = 'text'
    )
    return response
