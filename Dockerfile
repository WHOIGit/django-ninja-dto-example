FROM python:3.11-slim

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

RUN echo "DJANGO_NINJA_EXAMPLE_API_TOKEN=ac9bd5d8acca0b49db8d79c80fb899f136a0fa98" > ./.env
RUN echo "DJANGO_NINJA_EXAMPLE_ENDPOINT=http://localhost:80" >> ./.env

EXPOSE 80

ENV DJANGO_SUPERUSER_USERNAME="admin"
ENV DJANGO_SUPERUSER_PASSWORD="whoi1930"
ENV DJANGO_SUPERUSER_EMAIL="rajesh.mishra@whoi.edu"
ENTRYPOINT [ "sh", "-c", "cd ./example && python manage.py runserver 0.0.0.0:80" ]


