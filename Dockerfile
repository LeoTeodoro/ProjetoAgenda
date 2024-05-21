# Define nossa imagem base
FROM jenkins/jenkins:lts

# Define nosso usuario dentro do container
USER root

# Executa comandos para instalar o python
RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN pip install --target=c:\users\gabriel\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages coverage --upgrade

# Instalando mailutils
RUN apt-get install -y mailutils

USER jenkins