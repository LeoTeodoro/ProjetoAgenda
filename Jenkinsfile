pipeline {

    agent any

    stages {

        stage('Build'){

            steps {
                echo 'Building...'
                sh '''
                    python3 src/index.py
                '''
            }

        }

         stage('Test'){

            steps {
                echo 'Testing...'
                sh '''
                    coverage run src/agendaTest.py
                    coverage report
                    coverage html
                '''
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