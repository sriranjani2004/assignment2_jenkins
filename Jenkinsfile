pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sriranjani2004/flask-app"
        DOCKER_CREDENTIALS = "docker-hub"
        GIT_REPO = "https://github.com/sriranjani2004/assignment2_jenkins.git"
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Verify Docker Access') {
            steps {
                script {
                    sh "docker --version || { echo 'Docker is not installed or not accessible'; exit 1; }"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        echo "Building Docker Image..."
                        docker build -t ${DOCKER_IMAGE}:latest .
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh """
                        echo "Running Unit Tests..."
                        docker run --rm ${DOCKER_IMAGE}:latest python -m unittest test_app.py || { echo 'Tests failed'; exit 1; }
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    withDockerRegistry(credentialsId: DOCKER_CREDENTIALS, url: '') {
                        sh """
                            echo "Pushing Docker Image to Docker Hub..."
                            docker push ${DOCKER_IMAGE}:latest
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline Execution Successful!"
        }
        failure {
            echo "❌ Pipeline Execution Failed!"
        }
    }
}
