# Base image for Python
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

COPY ./blitz_project/requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY ./blitz_project /app/

# Expose Django's default port (8000)
EXPOSE 8000

# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
