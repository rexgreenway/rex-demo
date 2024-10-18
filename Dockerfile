FROM python:3.12 AS builder

# Maybe update to use pipx for this later
RUN pip install poetry==1.8.4

ENV POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /src

# Install deps using poetry
COPY pyproject.toml README.md /src/
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR


FROM python:3.12-slim AS runtime

WORKDIR /src

# Copy over and set up venv
ENV VIRTUAL_ENV=/src/.venv
COPY --from=builder /src/.venv /src/.venv
ENV PATH="/src/.venv/bin:$PATH"

# Copy add and start API
COPY ./app /src/app
CMD ["fastapi", "run", "app/main.py", "--port", "8080"]
