pipeline {
    agent any

    environment {
        // Define the service name for Django
        DJANGO_TEST_SERVICE = 'django'
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
                // Build Docker image for Django service
                sh 'docker-compose build $DJANGO_TEST_SERVICE'
            }
        }

        stage('Run Django Tests') {
            steps {
                // Run Django tests using the default test.py
                sh """
                docker-compose run --rm $DJANGO_TEST_SERVICE sh -c "python manage.py test"
                """
            }
        }

        stage('Cleanup') {
            steps {
                // Stop and remove containers, networks, and volumes
                sh 'docker-compose down --volumes --remove-orphans'
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
