pipeline {

    agent any
    parameters {

    choice(
        name: 'EXECUTION_TYPE',
        choices: ['UI', 'API', 'ALL'],
        description: 'Select Test Suite'
    )
    choice(
    name: 'BROWSER',
    choices: ['DEFAULT', 'CHROMIUM', 'FIREFOX', 'WEBKIT'],
    description: 'Browser'
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

         environment {

            ENVIRONMENT = "${params.ENVIRONMENT}"
            BROWSER = "${params.BROWSER == 'DEFAULT' ? '' : params.BROWSER.toLowerCase()}"

        }

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