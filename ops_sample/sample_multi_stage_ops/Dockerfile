FROM python:3.8 as base

RUN pip install poetry==1.1.7
RUN poetry config virtualenvs.create false

WORKDIR /opt/app
COPY src src
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

# development image
FROM base as development

COPY tests tests
RUN poetry install

ENTRYPOINT [ "pytest" ]

# production image
FROM base as production

RUN poetry install --no-dev

ENTRYPOINT [ "python", "src/main.py" ]
