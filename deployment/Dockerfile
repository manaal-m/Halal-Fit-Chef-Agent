# deployment/Dockerfile

# Use a specific Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies in the container environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
# This includes main.py, agents/, services/, tools/
COPY . .

# Command to run the agent when the container starts
# Assumes main.py is your entry point
CMD ["python", "main.py"]