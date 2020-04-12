FROM python:3.7-alpine as base

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /app
WORKDIR /app
EXPOSE 5000
ENV FLASK_APP main.py
CMD ["flask", "run"]
