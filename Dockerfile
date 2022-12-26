FROM python:3.9

# Allows docker to cache installed dependencies between builds

COPY project/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image

COPY project app
WORKDIR /app
ADD .env /env_file/.env

RUN python manage.py migrate
RUN python manage.py collectstatic
