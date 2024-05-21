FROM jenkins/jenkins:lts

USER root

# Atualizar os pacotes e instalar dependências
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Criar um ambiente virtual e ativá-lo
RUN python3 -m venv /opt/venv

# Ativar o ambiente virtual e instalar pipenv
RUN pip3 install pipenv

# instalação de mailutils
RUN apt-get install -y mailutils

USER jenkins