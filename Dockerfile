# Define nossa imagem base
FROM jenkins/jenkins:lts

ENV DEBIAN_FRONTEND=noninteractive

# Define nosso usuario dentro do container
USER root

# Executa comandos para instalar o python
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip3 install --upgrade pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

# Instalando mailutils
RUN apt-get install -y mailutils

USER jenkins

EXPOSE 8080

CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]