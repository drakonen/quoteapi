# Run the DEV server in a docker container, dont use for prod

# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
# RUN apt-get update && apt-get install -y \
#    libpq-dev \
#    gcc \
#    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy the requirements file
COPY pyproject.toml /app/
COPY uv.lock /app/

# Install Python dependencies
RUN uv sync

# Copy the project files (this also copies the testing DB file)
COPY . /app/

# Place executables in the virtual environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Run database migrations
RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# Start the Django DEV server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]