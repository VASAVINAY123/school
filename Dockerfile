# Use the official Python image as base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Optional: collect static files (for production)
# RUN python manage.py collectstatic --noinput

# Expose port (Django default)
EXPOSE 8000

# Start the Django development server (for production, use gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
