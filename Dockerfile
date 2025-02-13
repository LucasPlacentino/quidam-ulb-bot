# Use an official Python runtime as a parent image
FROM python:3.12-alpine
# alpine or slim ?

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Install any dependencies specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
#EXPOSE 8000

# Define environment variable
# Make the stdout and stderr streams unbuffered by setting the PYTHONUNBUFFERED environment variable to non-empty value different from 0 (recommended in containers):
ENV PYTHONUNBUFFERED=1

# Run app.py using python
#CMD ["uvicorn", "src/app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "src/app.py"]
