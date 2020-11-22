FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip && pip install flask gunicorn

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 my_site:app