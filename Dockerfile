FROM python:3.7.9
COPY . /app
RUN pip install gunicorn
WORKDIR /app
CMD ["gunicorn", "-w 3", "-b :8000", "http_server:Server"]