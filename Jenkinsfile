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
                git credentialsId: 'github-credentials', url: env.GIT_REPO, branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh "docker run --rm ${DOCKER_IMAGE}:latest python -m unittest test_app.py"
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    withDockerRegistry(credentialsId: DOCKER_CREDENTIALS, url: '') {
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline Execution Successful!"
        }
        failure {
            echo "Pipeline Execution Failed!"
        }
    }
}
