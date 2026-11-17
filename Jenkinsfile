pipeline {
    agent any

    environment {
        APP_NAME = 'pipeline'
        APP_PORT = '8081'
    }

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('1. Checkout') {
            steps {
                checkout scm
            }
        }

        stage('2. Tests unitaires') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python -m pytest --cov=. --cov-report=xml:coverage.xml
                '''
            }
        }

        stage('3. Analyse SonarQube') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('4. Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('5. Build image Docker') {
            steps {
                sh '''
                    docker build -t ${APP_NAME}:${BUILD_NUMBER} .
                    docker tag ${APP_NAME}:${BUILD_NUMBER} ${APP_NAME}:latest
                '''
            }
        }

        stage('6. Déploiement local') {
            steps {
                sh '''
                    docker rm -f ${APP_NAME} || true
                    docker run -d --name ${APP_NAME} -p ${APP_PORT}:8080 ${APP_NAME}:latest
                    sleep 3
                    curl -f http://localhost:${APP_PORT}/
                '''
            }
        }
    }

    post {
        success { echo "Déploiement réussi : http://localhost:${APP_PORT}" }
        failure { echo 'Pipeline en échec : consulte la console et SonarQube.' }
    }
}
