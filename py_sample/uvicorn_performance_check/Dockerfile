FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir && rm requirements.txt

COPY src /opt/app/
WORKDIR /opt/app
