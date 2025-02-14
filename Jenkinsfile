pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sriranjani2004/flask-app"
        DOCKER_CREDENTIALS = "docker-hub"
        GIT_REPO = "git@github.com:sriranjani2004/assignment2_jenkins.git"
        REMOTE_SERVER = "192.168.198.53"
        REMOTE_USER = "ariv"
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
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    withDockerRegistry(credentialsId: DOCKER_CREDENTIALS, url: '') {
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh """
                        ssh ${REMOTE_USER}@${REMOTE_SERVER} '
                        docker pull ${DOCKER_IMAGE}:latest &&
                        docker stop flask-app || true &&
                        docker rm flask-app || true &&
                        docker run -d -p 5000:5000 --name flask-app ${DOCKER_IMAGE}:latest
                        '
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Deployment Successful!"
        }
        failure {
            echo "Deployment Failed!"
        }
    }
}
