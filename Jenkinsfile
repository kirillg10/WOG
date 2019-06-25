pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kirillg10/WOG.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("kirillg10/score-server:latest")
                }
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker-compose down -v'
                sh 'docker-compose push'
            }
        }

    }
}
