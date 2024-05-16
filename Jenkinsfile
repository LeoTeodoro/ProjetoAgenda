pipeline {

    agent any

    stages {

        stage('Build'){

            steps {
                echo 'Building...'
                sh "python3.12 src/index.py"
            }

        }

    }

}