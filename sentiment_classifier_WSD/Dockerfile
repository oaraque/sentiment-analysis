FROM alpine:3.2

ADD repositories /etc/apk/repositories
RUN apk add --update python python-dev gfortran py-pip build-base py-numpy@testing

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt 

COPY . /app

VOLUME /input.txt
VOLUME /output.txt

CMD python run.py /input.txt /output.txt
