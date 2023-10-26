# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for your Django application
ENV DJANGO_SETTINGS_MODULE=myapp.settings
ENV DEBUG=False

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Expose port 8000 for the Django development server (you can change this port)
EXPOSE 8000



# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
