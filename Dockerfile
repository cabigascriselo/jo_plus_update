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

#2 Use an official Python runtime as a parent image
#FROM python:3.10-slim
FROM python:3.11

#3 Set the working directory in the container
WORKDIR /app

#4 Copy the requirements.txt file into the container
COPY requirements.txt /app/

#5 Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#6 Copy the current directory contents into the container at /app
COPY . /app/

#7 Expose the port the app runs on
EXPOSE 8000

#8 Command to run the Django development server (for local development)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
