FROM python:3.7-alpine as base

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /app
WORKDIR /app
EXPOSE 5000
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["flask", "run"]
