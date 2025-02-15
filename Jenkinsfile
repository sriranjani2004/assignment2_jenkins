pipeline {
    agent any

    environment {
        IMAGE_NAME = "sriranjani2809/flask-app"
        CONTAINER_NAME = "eloquent_mirzakhani"
    }

    stages {
        stage('Check Docker') {
            steps {
                sh '''
                    echo "🔹 Checking Docker availability..."
                    export PATH=$PATH:/usr/local/bin
                    if ! command -v docker &> /dev/null; then
                        echo "❌ Docker is not installed or not in PATH!"
                        exit 1
                    fi
                    docker version
                '''
            }
        }

        stage('Clone Repository') {
            steps {
                git credentialsId: 'gitlab-credentials', url: 'https://github.com/sriranjani2004/assignment2_jenkins.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "🔹 Installing Python dependencies..."
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "🔹 Running tests..."
                    source venv/bin/activate
                    python -m unittest discover tests
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "🔹 Building Docker image..."
                    export PATH=$PATH:/usr/local/bin
                    docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    echo "🔹 Stopping and removing existing container (if any)..."
                    export PATH=$PATH:/usr/local/bin
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true

                    echo "🔹 Deploying new container..."
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
