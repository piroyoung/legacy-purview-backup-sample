FROM python:alpine3.19

RUN apk update && apk add gcc \
    libc-dev \
    libffi-dev

RUN pip install poetry

COPY pvsnapshot /local/pvsnapshot/pvsnapshot
COPY main.py /local/pvsnapshot/main.py
COPY pyproject.toml /local/pvsnapshot/pyproject.toml

WORKDIR /local/pvsnapshot
RUN poetry install

ENV CLIENT_ID="client_id"
ENV CLIENT_SECRET="client_secret"
ENV TENANT_ID="tenant_id"
ENV PURVIEW_ENDPOINT="purview_endpoint"

WORKDIR /local/pvsnapshot
ENTRYPOINT ["poetry", "run", "python", "main.py"]
