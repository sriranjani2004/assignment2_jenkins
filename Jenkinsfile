pipeline {
    agent any

    tools {
        python "Python3" // Ensure Jenkins uses the installed Python
    }

    environment {
        IMAGE_NAME = "sriranjani2809/flask-app"
        CONTAINER_NAME = "eloquent_mirzakhani"
    }

    stages {
        stage('Check Docker') {
            steps {
                sh 'docker version'
            }
        }

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/sriranjani/assignment2_jenkins'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                '''
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline Execution Completed"
        }
        failure {
            echo "❌ Build Failed!"
        }
    }
}