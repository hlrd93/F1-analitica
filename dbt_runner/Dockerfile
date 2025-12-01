FROM python:3.9-slim

# Minimal deps for dbt + clickhouse adapter
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential git curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY ./requirements-dbt.txt /tmp/requirements-dbt.txt
RUN pip install --no-cache-dir -r /tmp/requirements-dbt.txt

# Keep a small default shell entrypoint; command overridden by docker-compose
ENTRYPOINT ["/bin/bash", "-lc"]
CMD ["/bin/bash"]
