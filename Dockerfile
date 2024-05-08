FROM python:alpine3.19

RUN apk update && apk add gcc \
    libc-dev \
    libffi-dev

RUN pip install poetry

COPY purview-util /local/purview-util
COPY main.py /local/main.py
COPY pyproject.toml /local/pyproject.toml

WORKDIR /local/purview-util
RUN poetry install

WORKDIR /local
CMD ["poetry", "run", "python", "main.py"]

