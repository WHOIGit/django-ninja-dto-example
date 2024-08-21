FROM python:3.11-slim

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/example
COPY ./example .

EXPOSE 80

CMD python manage.py runserver 0.0.0.0:80
