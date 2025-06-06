FROM python:3.13-alpine
LABEL authors="simane988"

# SOME ENVS
ENV POETRY_VIRTUALENVS_CREATE=false

# Install poetry
# Install and setup poetry
RUN pip install -U pip poetry && \
    apk add --no-cache ffmpeg
ENV PATH="${PATH}:/root/.poetry/bin"

# Copy only poetry stuff
WORKDIR /app
COPY video_converter/poetry.lock video_converter/pyproject.toml ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY video_converter/app ./

ENTRYPOINT ["python3","app.py"]
