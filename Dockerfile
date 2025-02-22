# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variables
ENV PORT 8080

# Expose the port the application runs on
EXPOSE $PORT

# Set the entry point to run gunicorn
CMD ["gunicorn", "-b", ":8080", "shinoda:app"]