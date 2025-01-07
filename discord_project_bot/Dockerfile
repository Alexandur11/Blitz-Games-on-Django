# Base image for Python
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY ./discord_project_bot/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./discord_project_bot /app/

# Set the default command to run the Discord bot
CMD ["python", "main.py"]
