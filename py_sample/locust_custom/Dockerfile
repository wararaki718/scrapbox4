FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /opt/api
COPY api /opt/api

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
