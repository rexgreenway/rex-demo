FROM python:3.12

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - 
    
ENV PATH="/root/.local/bin:$PATH"
RUN poetry --version

WORKDIR /code

COPY pyproject.toml README.md /code/

RUN poetry install --no-root

COPY ./app /code/app

CMD ["poetry", "run", "fastapi", "run", "--port", "80"]

# CMD ["poetry", "run", "fastapi", "run", "app/main.py", "--port", "8080"]