# Dockerfile
FROM python:3.9.10-alpine3.14
WORKDIR .
RUN pip install --upgrade pip
RUN pip install flask
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=app
CMD ["python","main.py"]