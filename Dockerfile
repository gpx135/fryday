# Stage 1: Build the frontend
FROM node:14-alpine as frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Set up the backend
FROM python:3.11

ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
WORKDIR /code

# Install backend dependencies
COPY backend/requirements.txt /code/
RUN pip install -r requirements.txt

# Copy backend code
COPY backend/ /code/

# Copy frontend build to backend static files
COPY --from=frontend /app/frontend/build /code/static/

# Default command
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
