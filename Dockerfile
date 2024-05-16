# Define nossa imagem base
FROM jenkins/jenkins:lts

# Define nosso usuario dentro do container
USER root

# Executa comandos para instalar o python
RUN apt-get update && \
    apt-get install -y python3 python3-pip