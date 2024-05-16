# Define nossa imagem base
FROM jenkins/jenkins:lts

# Define nosso usuario dentro do container
USER root

# Executa comandos para instalar o python
RUN pip install --no-cache-dir flask requests