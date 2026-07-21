pipeline {
    agent any

    tools {
        maven 'maven'    // Must exactly match the name in Global Tool Configuration
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
}
