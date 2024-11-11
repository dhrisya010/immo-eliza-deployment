# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all contents from the api directory into /app in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r api/requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:immoapp", "--host", "0.0.0.0", "--port", "8000"]