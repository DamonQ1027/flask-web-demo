FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root --only main

COPY . /app

EXPOSE 5000
CMD ["poetry", "run", "python", "app.py"]
