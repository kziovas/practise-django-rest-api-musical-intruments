FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "manage.py", "migrate", ";","python3", "manage.py", "makemigrations",";","python3", "manage.py", "runserver", "0.0.0.0:8080" ]