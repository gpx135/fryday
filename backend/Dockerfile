FROM python:3.11

ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project code
COPY . /code/


# Default command
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]