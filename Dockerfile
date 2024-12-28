# Use the official Python image as the base image
#FROM python:3.8

# Set the working directory in the container
#WORKDIR /app

# Copy the application files into the working directory
#COPY . /app

# Install the application dependencies
#RUN pip install -r requirements.txt

# Define the entry point for the container
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#o build your container
#docker build -t python-django-app .

#to run the container
#docker run -it -p 8000:8000 python-django-app

#Container IDs
#docker ps -a

#To turn off your Docker container
#docker stop container_id

# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "joplus.wsgi:application"]
