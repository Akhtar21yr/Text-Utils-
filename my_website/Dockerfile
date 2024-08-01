FROM python:3.9

# Set working directory
WORKDIR /app/backend

# Install dependencies
COPY requirements.txt /app/backend/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/backend/

# Expose port
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
