pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Starting the Build stage...'
                // Add your build commands here
                echo 'Build completed successfully!'
            }
        }

        stage('Test') {
            steps {
                echo 'Starting the Test stage...'
                // Add your test commands here
                echo 'Tests executed successfully!'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting the Deploy stage...'
                // Add your deployment commands here
                echo 'Application deployed successfully!'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
