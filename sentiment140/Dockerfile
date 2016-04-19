FROM alpine:latest
MAINTAINER Oscar Araque

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

VOLUME /input.txt
VOLUME /output.txt

CMD curl --data-binary @/input.txt "http://www.sentiment140.com/api/bulkClassify" > /output.txt
