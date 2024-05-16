pipeline {

    agent any

    stages {

        stage('Build'){

            steps {
                echo 'Building...'
                sh "python3.12 src/index.py"
            }

        }

         stage('Test'){

            steps {
                echo 'Testing...'
                sh "python3.12 src/agendaTest.py"
            }

        }
    }

}