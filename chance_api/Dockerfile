# Dockerfile for a Python App
FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5003
ENTRYPOINT ["python3", "app.py"]