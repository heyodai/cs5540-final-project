# Set the base image
FROM python:3.9-slim-buster

# Install pandoc and texlive (if you need LaTeX support)
RUN apt-get update && apt-get install -y pandoc texlive

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the necessary packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script and run it by default
COPY convert.py .
CMD ["python", "convert.py"]
