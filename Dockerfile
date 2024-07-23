# Stage 1: Build frontend
FROM node:18 AS frontend-builder
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Build backend
FROM python:3.11 AS backend-builder
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY backend/requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ /code/

# Stage 3: Combine frontend and backend into final image
FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# Install Nginx and Gunicorn
RUN apt-get update && apt-get install -y nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip install gunicorn

# Copy backend build and installed packages
COPY --from=backend-builder /code /code
COPY --from=backend-builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy frontend build
COPY --from=frontend-builder /app/.next /code/static/frontend/.next
COPY --from=frontend-builder /app/public /code/static/frontend/public

# Set environment variables for Django
ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_HOST
ARG POSTGRES_PORT
ARG DJANGO_SECRET_KEY
ARG DJANGO_DEBUG
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD
ENV POSTGRES_DB=$POSTGRES_DB
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_HOST=$POSTGRES_HOST
ENV POSTGRES_PORT=$POSTGRES_PORT
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV DJANGO_DEBUG=$DJANGO_DEBUG
ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create entrypoint script
RUN echo '#!/bin/sh\n' \
    'set -e\n' \
    'echo "Running migrations..."\n' \
    'python manage.py migrate\n' \
    'echo "Collecting static files..."\n' \
    'python manage.py collectstatic --noinput\n' \
    'echo "Starting Gunicorn..."\n' \
    'gunicorn --bind 0.0.0.0:8000 fryday_project.wsgi:application &\n' \
    'echo "Starting Nginx..."\n' \
    'nginx -g "daemon off;"\n' \
    > /code/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Expose port 80
EXPOSE 80

# Start the entrypoint script
CMD ["/code/entrypoint.sh"]
