FROM python:2.7-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

VOLUME /input.txt
VOLUME /output.txt

CMD python run.py
