import { Construct } from 'constructs';
import { aws_ssm as ssm } from 'aws-cdk-lib';
import { flatten } from 'flat';

export interface AppParametersProps {
    appName: string;
    filePath: string;
}

export class AppParameters extends Construct {
    constructor(scope: Construct, id: string, props: AppParametersProps) {
        super(scope, id);

        const json_params = require(props.filePath);
        const params: { [key: string]: string; } = flatten(json_params, { delimiter: '/', safe: true });

        for (const path of Object.keys(params)) {
            const parameterName = `/${props.appName}/${path}`;
            const stringValue = params[path];
            new ssm.StringParameter(this, parameterName, { stringValue, parameterName });
        }
    }
}