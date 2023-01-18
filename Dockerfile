FROM python:3.10-slim

# Change working directory
WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app


# Copy source code
COPY ./dagster.yaml ./workspace.yaml ./
COPY  ./dagster_example ./dagster_example


# Install dependencies
COPY ./pyproject.toml .
COPY ./LICENSE .
COPY ./README.md .
RUN pip install .


CMD ["dagit", "-w", "workspace.yaml", "-h", "0.0.0.0", "-p", "3333"]
