# Base image
FROM python:3.10-slim

# Install system dependencies for ZAP and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    openjdk-21-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the Flask app & requirements(included already)
COPY Security_Compliance_workshop-rishika/day3/app/ ./app


# Install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r app/requirements.txt bandit semgrep
RUN pip install bandit pbr semgrep


# Expose port for Flask app
EXPOSE 8000

# Default command (runs Flask app)
CMD ["python", "app/app.py"]

