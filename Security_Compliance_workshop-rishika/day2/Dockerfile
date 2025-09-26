# Use Python 3.11 as base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy day2 folder contents into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port your app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
