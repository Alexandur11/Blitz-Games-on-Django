# Base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot's source code
COPY . /app/

# Command to run the Discord bot
CMD ["python", "main.py"]
