FROM python:3.8-slim-buster

ARG SCOPE

# Setup env
ENV SCOPE=${SCOPE} \
  # python
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  LC_ALL=C.UTF-8 \
  LANG=C.UTF-8 \
  # pip
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.1.13 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local'

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    curl \
    build-essential \
    default-libmysqlclient-dev \
    libpq-dev \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$SCOPE" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

CMD ["/code/commands/run-prod.sh"]
