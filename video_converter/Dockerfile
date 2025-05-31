FROM python:3.13-alpine
LABEL authors="simane988"

# ENVS
ENV POETRY_VIRTUALENVS_CREATE=false

# Install poetry
# Install and setup poetry
RUN pip install -U pip poetry && \
    apk add --no-cache ffmpeg
ENV PATH="${PATH}:/root/.poetry/bin"

# Copy only poetry stuff
WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY app ./

ENTRYPOINT ["python3","app.py"]