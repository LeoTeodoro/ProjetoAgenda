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
                    pipenv coverage install --dev
                    pipenv run coverage html
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
        // stage('Notification'){

        //     steps {
        //         script {
        //             echo 'Notification'
        //             emailext body: '''<p>Relatório de testes gerado pelo Jenkins.</p>
        //                             <p>Veja o relatório de cobertura de testes no link a seguir:</p>
        //                             <p><a href="${BUILD_URL}htmlcov/index.html">Relatório de Cobertura</a></p>''',
        //                      subject: "Relatório de Testes - Build #${BUILD_NUMBER}",
        //                      to: 'gabriel.leal@gec.inatel.br',
        //                      mimeType: 'text/html'
        //         }
        //     }
        // }
    }

}