pipeline {

    agent any
    parameters {

    choice(
        name: 'EXECUTION_TYPE',
        choices: ['UI', 'API', 'ALL'],
        description: 'Select Test Suite'
    )

}

    stages {

        stage('Checkout') {

            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {

            steps {
                bat 'scripts\\setup_environment.bat'
            }
        }

        stage('Execute Framework') {

            steps {
                bat "scripts\\run_framework.bat ${params.EXECUTION_TYPE.toLowerCase()} jenkins"
            }
        }
    }

    post {

        always {

            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'artifacts/allure-results']]
            )

            archiveArtifacts(
                artifacts: 'artifacts/**/*',
                fingerprint: true
            )
        }
    }
}