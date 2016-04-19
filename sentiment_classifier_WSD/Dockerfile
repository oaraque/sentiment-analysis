FROM alpine:3.2
MAINTAINER Oscar Araque

ADD repositories /etc/apk/repositories
RUN apk add --update python python-dev gfortran py-pip build-base py-numpy@testing

RUN mkdir /app
RUN mkdir -p /usr/share/nltk_data
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt 

# nltk packages won't download
# RUN python -m nltk.downloader wordnet punkt
RUN mkdir -p /usr/share/nltk_data/corpora; mkdir -p /usr/share/nltk_data/tokenizers
WORKDIR /usr/share/nltk_data/corpora
RUN wget www.nltk.org/nltk_data/packages/corpora/wordnet.zip
RUN unzip wordnet.zip && rm wordnet.zip
WORKDIR /usr/share/nltk_data/tokenizers
RUN wget http://www.nltk.org/nltk_data/packages/tokenizers/punkt.zip	 
RUN unzip punkt.zip && rm punkt.zip
WORKDIR /app

COPY . /app

VOLUME /input.txt
VOLUME /output.txt

CMD python run.py /input.txt /output.txt
