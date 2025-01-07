pipeline {
    agent any

    environment {
        // Define the image name for Django
        DJANGO_IMAGE = 'django_app_image'
        DJANGO_TEST_SERVICE = 'django'  // Service name is just for reference
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image for the Django application
                    sh 'docker build -t $DJANGO_IMAGE .'
                }
            }
        }

        stage('Run Django Tests') {
            steps {
                script {
                    // Run Django tests using the Docker container
                    sh """
                    docker run --rm $DJANGO_IMAGE python manage.py test
                    """
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Optionally stop any containers or remove images if needed
                    sh 'docker image prune -f'
                }
            }
        }
    }

    post {
        always {
            // Always clean up Docker resources after pipeline execution
            sh 'docker system prune -f'
        }
        success {
            echo 'Django tests passed successfully!'
        }
        failure {
            echo 'Django tests failed. Please check the logs for details.'
        }
    }
}
