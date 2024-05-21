pipeline {

    agent any

    stages {

        stage('Build'){

            steps {
                echo 'Building...'
                sh "python3 src/index.py"
            }

        }

         stage('Test'){

            steps {
                echo 'Testing...'
                sh "python3 src/agendaTest.py"
                archiveArtifacts 'htmlcov/index.html'
            }

        }
        stage('Notification'){

            steps {
                echo 'Notification...'
                sh '''
                   cd src
                   mail -s "email enviado" gabriel.leal@gec.inatel.br
                   '''
            }
        }
    }

}