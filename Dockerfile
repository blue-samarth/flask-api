FROM python:3.12-slim AS builder

WORKDIR /app
RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

RUN ls -la .venv/bin && cat uv.lock


FROM python:3.12-slim AS runtime
WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

#This copies the uv binary from the builder stage to the runtime stage
COPY --from=builder /usr/local/bin/uv /usr/local/bin/uv 

COPY src/ src/

# RUN uv pip install gunicorn

ENV VIRTUAL_ENV="/app/.venv" \
    PATH="/app/.venv/bin:$PATH" \
    MONGO_URI="mongodb://mongodb:27017/users"

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "src.server:app"]
