# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's files into the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the app when the container starts
CMD ["python", "app.py"]
