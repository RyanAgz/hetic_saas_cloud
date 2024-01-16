FROM python:3.9.13

ENV APP_HOME /app
WORKDIR $APP_HOME

# WORKDIR /app:

# RUN apt-get update
COPY requirements .

RUN pip install -r requirements

COPY . .
CMD ["python3", "app.py"]