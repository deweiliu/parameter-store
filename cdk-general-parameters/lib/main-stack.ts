import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AppParameters } from './app-parameters';
import { readdirSync } from 'fs';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const dir = "../parameters/";
    readdirSync(dir).forEach(file => {
      const appName = file.split('.')[0];
      const filePath = `../${dir}${file}`

      new AppParameters(this, appName, { appName, filePath });
    });
  }
}
