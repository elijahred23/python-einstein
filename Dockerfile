# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install necessary packages, including Vim
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    vim \      
    && apt-get clean

# Install any needed packages specified in requirements.txt
COPY requirements.txt .

RUN pip3 install -r requirements.txt
# Set the working directory to /app/scripts
WORKDIR /app/scripts



