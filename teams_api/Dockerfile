# Dockerfile for a Python App
FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5001
ENTRYPOINT ["python3", "app.py"]