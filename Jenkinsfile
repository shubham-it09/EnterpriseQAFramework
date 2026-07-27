/*
==============================================================
 Enterprise QA Framework Pipeline
 Author : Shubham Pandey
==============================================================

This pipeline performs:

1. Checkout latest code from GitHub
2. Setup Python Environment
3. Execute requested test suite
4. Publish Allure Report
5. Archive Execution Artifacts

Future Enhancements:
--------------------
✓ Parallel UI/API Execution
✓ Docker
✓ Retry
✓ Notifications
✓ GitHub Actions
✓ Azure DevOps

==============================================================
*/

pipeline {

    /*
    ----------------------------------------------------------
    Agent
    ----------------------------------------------------------
    Defines where this pipeline should execute.

    'any' means Jenkins can run this pipeline
    on any available agent/node.

    Future:
        agent { label 'windows' }
        agent { label 'linux' }

    ----------------------------------------------------------
    */

    agent any


    /*
    ----------------------------------------------------------
    Pipeline Options
    ----------------------------------------------------------
    Global pipeline behaviour.

    These options apply to the entire pipeline.

    ----------------------------------------------------------
    */

    options {

        /*
        Add timestamps to every console log.

        Example:

        10:35:21  Running Tests...
        10:36:02  Generating Report...
        */

        timestamps()


        /*
        Prevent multiple executions of this pipeline
        at the same time.

        If Build #15 is running,
        Build #16 waits until Build #15 completes.

        Prevents:
            • Workspace corruption
            • Allure conflicts
            • Screenshot conflicts
            • Log conflicts
        */

        disableConcurrentBuilds()


        /*
        Automatically clean old Jenkins builds.

        Keep:
            Last 20 builds
            Last 10 build artifacts

        Prevents Jenkins disk from filling up.
        */

        buildDiscarder(
            logRotator(
                numToKeepStr: '20',
                artifactNumToKeepStr: '10'
            )
        )


        /*
        Abort the pipeline if it runs
        longer than 60 minutes.

        Prevents hung executions.
        */

        timeout(
            time: 60,
            unit: 'MINUTES'
        )

    }

    triggers {

        cron('H 2 * * *')

    }


    /*
    ----------------------------------------------------------
    Build Parameters
    ----------------------------------------------------------
    Values selected by the user before the pipeline starts.

    Jenkins UI:

    Build With Parameters

        Execution Type
        Environment
        Browser

    ----------------------------------------------------------
    */

    parameters {

        /*
        Select which test suite to execute.
        */

        choice(
            name: 'EXECUTION_TYPE',
            choices: ['UI', 'API', 'ALL'],
            description: 'Select Test Suite'
        )


        /*
        Select execution environment.

        Used by ConfigManager to load:

            qa.yaml
            uat.yaml
            prod.yaml
        */

        choice(
            name: 'ENVIRONMENT',
            choices: ['QA', 'UAT', 'PROD'],
            description: 'Execution Environment'
        )


        /*
        Browser Override.

        DEFAULT
            → Uses browser defined in YAML

        Others
            → Override browser at runtime
        */

        choice(
            name: 'BROWSER',
            choices: ['DEFAULT', 'CHROMIUM', 'FIREFOX', 'WEBKIT','ALL'],
            description: 'Browser'
        )

    }



    /*
    ----------------------------------------------------------
    Pipeline Stages
    ----------------------------------------------------------
    Stages represent the high level execution flow.

    ----------------------------------------------------------
    */

    stages {


        /*
        ------------------------------------------------------
        Stage : Checkout
        ------------------------------------------------------

        Download latest source code from GitHub.

        Equivalent to:

            git clone
            git pull

        ------------------------------------------------------
        */

        stage('Checkout') {

            steps {

                checkout scm

            }

        }

        /*
----------------------------------------------------------
Stage : Build Information
----------------------------------------------------------

Customize Jenkins build name.

Example:

#25 QA | UI | CHROMIUM

----------------------------------------------------------
*/

stage('Build Information') {

    steps {

        script {

            currentBuild.displayName =
                "#${env.BUILD_NUMBER} | " +
                "${params.ENVIRONMENT} | " +
                "${params.EXECUTION_TYPE} | " +
                "${params.BROWSER}"
            currentBuild.description =
                    "Environment: ${params.ENVIRONMENT}<br>" +
                    "Execution: ${params.EXECUTION_TYPE}<br>" +
                    "Browser: ${params.BROWSER}"

                }

            }

        }


        /*
        ------------------------------------------------------
        Stage : Setup Environment
        ------------------------------------------------------

        Creates Virtual Environment (if required)

        Installs:

            Python Packages
            Playwright Browsers

        Verifies framework installation.

        ------------------------------------------------------
        */

        stage('Setup Environment') {

            steps {

                bat 'scripts\\setup_environment.bat'

            }

        }

        stage('Clean Reports') {

            steps {

                bat 'scripts\\clean_reports.bat'

            }

        }


       /*
----------------------------------------------------------
Stage : Execute Tests
----------------------------------------------------------

Runs UI/API test suites.

Execution Type

UI  -> UI only

API -> API only

ALL -> UI and API in parallel

----------------------------------------------------------
*/

stage('Execute Tests') {

    parallel  {
        

        stage('Run UI Tests') {

            when {

                anyOf {

                    expression {
                        params.EXECUTION_TYPE == 'UI'
                    }

                    expression {
                        params.EXECUTION_TYPE == 'ALL'
                    }

                }

            }

            steps {

                script {

                    env.ENVIRONMENT =
                        params.ENVIRONMENT.toLowerCase()

                    env.BROWSER =
                        params.BROWSER == 'DEFAULT'
                        ? ''
                        : params.BROWSER.toLowerCase()

                }
                
                

                 bat 'scripts\\run_framework.bat ui jenkins'

                 
                

            }

        }

        stage('Run API Tests') {

            when {

                anyOf {

                    expression {
                        params.EXECUTION_TYPE == 'API'
                    }

                    expression {
                        params.EXECUTION_TYPE == 'ALL'
                    }

                }

            }

            steps {

                script {

                    env.ENVIRONMENT =
                        params.ENVIRONMENT.toLowerCase()

                    env.BROWSER =
                        params.BROWSER == 'DEFAULT'
                        ? ''
                        : params.BROWSER.toLowerCase()

                }
               
                    bat 'scripts\\run_framework.bat api jenkins'
                
                

            }

        }

    }

}
    }


    /*
    ----------------------------------------------------------
    Post Actions
    ----------------------------------------------------------

    Executes AFTER the pipeline.

    Even if tests fail.

    ----------------------------------------------------------
    */

   post {

            always {

                /*
                Generate Allure Report.
                */

                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'artifacts/allure-results']]
                )

                /*
                Archive execution artifacts.
                */

                archiveArtifacts(
                    artifacts: 'artifacts/**/*',
                    fingerprint: true
                )
            }

            success {

                emailext(
                    to: 'shubham.it09@gmail.com',
                    subject: "✅ SUCCESS - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
        Build Status : SUCCESS

        Job Name     : ${env.JOB_NAME}
        Build Number : ${env.BUILD_NUMBER}

        Environment  : ${params.ENVIRONMENT}
        Execution    : ${params.EXECUTION_TYPE}
        Browser      : ${params.BROWSER}

        Build URL:
        ${env.BUILD_URL}
        """
                )

            }

            failure {

                emailext(
                    to: 'shubham.it09@gmail.com',
                    subject: "❌ FAILURE - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
        Build Status : FAILURE

        Job Name     : ${env.JOB_NAME}
        Build Number : ${env.BUILD_NUMBER}

        Environment  : ${params.ENVIRONMENT}
        Execution    : ${params.EXECUTION_TYPE}
        Browser      : ${params.BROWSER}

        Build URL:
        ${env.BUILD_URL}
        """
                )

            }

        }

}