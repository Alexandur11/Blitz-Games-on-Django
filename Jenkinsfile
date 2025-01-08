pipeline {
    agent any

    environment {
        // Define the Docker image name for Django
        DJANGO_IMAGE = 'blitz_games_django_image'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the root directory
                    sh 'docker build -t $DJANGO_IMAGE .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run Django tests inside the Docker container
                    sh """
                    docker run --rm $DJANGO_IMAGE python manage.py test
                    """
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Clean up unused Docker images and containers
                    sh 'docker system prune -f --volumes'
                }
            }
        }
    }

    post {
        always {
            // Ensure cleanup runs even if the pipeline fails
            sh 'docker system prune -f --volumes'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the logs for more details.'
        }
    }
}
