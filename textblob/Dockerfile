FROM alpine:latest
MAINTAINER Oscar Araque

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \ 
    pip3 install --upgrade pip setuptools && \ 
    rm -r /root/.cache

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt 

# nltk packages won't download
# RUN python3 -m textblob.download_corpora lite
 RUN mkdir -p /usr/share/nltk_data/corpora && \ 
     mkdir -p /usr/share/nltk_data/tokenizers && \
     mkdir -p /usr/share/nltk_data/taggers
WORKDIR /usr/share/nltk_data/corpora
RUN wget www.nltk.org/nltk_data/packages/corpora/brown.zip
RUN unzip brown.zip && rm brown.zip
WORKDIR /usr/share/nltk_data/corpora
RUN wget www.nltk.org/nltk_data/packages/corpora/wordnet.zip
RUN unzip wordnet.zip && rm wordnet.zip
WORKDIR /usr/share/nltk_data/tokenizers
RUN wget www.nltk.org/nltk_data/packages/tokenizers/punkt.zip
RUN unzip punkt.zip && rm punkt.zip
WORKDIR /usr/share/nltk_data/taggers
RUN wget www.nltk.org/nltk_data/packages/taggers/averaged_perceptron_tagger.zip
RUN unzip averaged_perceptron_tagger.zip && rm averaged_perceptron_tagger.zip

WORKDIR /app

COPY . /app

VOLUME /input.txt
VOLUME /output.txt

CMD python3 run.py /input.txt /output.txt
