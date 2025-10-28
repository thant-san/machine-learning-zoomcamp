# Use the base image provided
FROM svizor/zoomcamp-model:3.11.5-slim

# Set the working directory
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy the Pipenv files
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install dependencies from Pipfile.lock into the system
# --system: Install to system python, not a venv
# --deploy: Fail if Pipfile.lock is out of sync
RUN pipenv install --system --deploy

# Copy your Flask application script
# We are copying the predict.py file
COPY ["predict.py", "./"]

# Expose the port the app will run on
EXPOSE 9696

# Define the command to run the application
CMD ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
