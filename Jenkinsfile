pipeline {

    agent any

    stages {

        stage('Build'){

            steps {
                echo 'Building...'
                sh 'python3 src/index.py'
            }

        }

         stage('Test'){

            steps {
                echo 'Testing...'
                sh '''
                    python3 -m coverage run src/agendaTest.py
                    python3 -m coverage report
                    python3 -m coverage html
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