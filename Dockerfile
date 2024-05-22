FROM jenkins/jenkins:lts

USER root

# Atualizar os pacotes e instalar dependências
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

# Criar um ambiente virtual e ativá-lo
RUN python3 -m venv /opt/venv

# Ativar o ambiente virtual e instalar pipenv
RUN /opt/venv/bin/pip3 install pipenv

# Adicionar o caminho do ambiente virtual ao PATH
ENV PATH="/opt/venv/bin:$PATH"

# instalação de mailutils
RUN apt-get install -y mailutils

USER jenkins