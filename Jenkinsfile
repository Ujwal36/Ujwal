pipeline {
    agent any
    tools {
            maven 'maven-3.9.12'
            jdk 'jdk17'
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
