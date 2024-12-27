FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

# Set the working directory
WORKDIR /app

# Copy your application code into the container
COPY . .

# Install system dependencies, including FFmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install transformers boto3 runpod

# Command to run your application
CMD ["python", "rp_handler.py"]
