pipeline {

    agent any

    environment {
        PIPENV_VENV_IN_PROJECT = "true"
    }

    stages {

        stage('Build'){

            steps {
                echo 'Building...'
                sh '''
                    pipenv install --dev
                    python3 src/index.py
                '''
            }

        }

         stage('Test'){

            steps {
                script {
                    echo 'Testing...'
                    sh '''
                        cd src
                        pipenv run coverage run -m unittest agendaTest.py 
                        pipenv run coverage html
                    '''
                }
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