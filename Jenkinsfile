pipeline {
    agent {
        label 'deployer-slave-amazon-linux'
    }
    
    options {
        timeout(time: 30, unit: 'MINUTES')
        timestamps ()
    }

    stages {
        stage('Wait for Stack Ready'){
            steps{
                sh(script: 'aws cloudformation wait stack-update-complete --region eu-west-2 --stack-name ParameterStore', returnStatus: true)
            }
        }
        
        stage('CDK Deploy'){
            steps{
                dir('cdk-general-parameters'){
                    sh '''
                    npm install;
                    npm run deploy;
                    '''
                }
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}
