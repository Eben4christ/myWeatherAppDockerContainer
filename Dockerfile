# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV FLASK_APP=server.py
ENV FLASK_ENV=production

# Expose the port Flask is running on
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
