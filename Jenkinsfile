pipeline {
    agent any

    environment {
        DEVELOPMENT_ID = 'YOUR_DEVELOPMENT_TEAM_ID' // Replace with your development team ID
        CODE_SIGN_PASS = 'YOUR_KEYCHAIN_PASSWORD'  // Replace with your keychain password
        PROJECT_PATH = 'path/to/your.xcodeproj'    // Path to your Xcode project
        SCHEME = 'YourSchemeName'                 // Replace with your scheme name
        OUTPUT_DIR = 'build/ipa'                  // Directory for .ipa output
    }

    stages {
        stage('Build') {
            steps {
                echo 'Starting the Build stage...'
                sh '''
                python3 scripts/build.py \
                --development-id $DEVELOPMENT_ID \
                --code-sign-pass $CODE_SIGN_PASS \
                --project-path $PROJECT_PATH \
                --scheme $SCHEME \
                --output-dir $OUTPUT_DIR
                '''
                echo 'Build stage completed successfully!'
            }
        }

        stage('Test') {
            steps {
                echo 'Starting the Test stage...'
                sh '''
                python3 scripts/test.py \
                --development-id $DEVELOPMENT_ID \
                --project-path $PROJECT_PATH \
                --scheme $SCHEME
                '''
                echo 'Test stage completed successfully!'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting the Deploy stage...'
                sh '''
                python3 scripts/deploy.py \
                --archive-path $OUTPUT_DIR/YourApp.xcarchive \
                --output-dir $OUTPUT_DIR \
                --export-options-plist path/to/ExportOptions.plist
                '''
                echo 'Deploy stage completed successfully!'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
