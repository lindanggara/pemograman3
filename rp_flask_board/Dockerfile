# syntax=docker/dockerfile:1
FROM python:3.10-alpine

# Set working directory
WORKDIR /flask

# Install dependencies for building Python packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements file & install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 5000
EXPOSE 5000

# Start the Flask app
CMD ["python", "-m", "flask", "--app", "board", "run", "--host=0.0.0.0", "--debug"]

