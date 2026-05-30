FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask flask_sqlalchemy pymysql gunicorn werkzeug

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
