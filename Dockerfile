# Use an official Python runtime as a parent image
FROM python:3.11
LABEL authors="jonnyruffles"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# RUN apt update && apt install nodejs npm openssl g++ make -y && rm -rf /var/cache/apk/*

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Fixes: https://github.com/RobertCraigie/prisma-client-py/issues/835
RUN PRISMA_BINARY_CACHE_DIR=/.binaries prisma generate

# Generate prisma
RUN poetry run prisma generate --schema=./opspy_job_scraper/schema.prisma

# Define environment variable
ENV DATABASE_URL ""

# Run app.py when the container launches
# CMD ["python", "opspy_job_scraper/__init__.py"]
CMD ["poetry", "run", "python3", "opspy_job_scraper/__init__.py"]
