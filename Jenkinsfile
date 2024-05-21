pipeline {

    agent any

    stages {

        stage('Build'){

            steps {
                echo 'Building...'
                sh 'python src/index.py'
            }

        }

         stage('Test'){

            steps {
                echo 'Testing...'
                sh '''
                    python -m coverage run src/agendaTest.py
                    python -m coverage report
                    python -m coverage html
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