FROM python:3.8

COPY src /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "main.py"]
