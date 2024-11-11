# Step 1: Use an official Python image as a base
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the application code into the container
COPY . /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port on which the FastAPI app will run
EXPOSE 8000

# Step 6: Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:immoapp", "--host", "0.0.0.0", "--port", "8000"]