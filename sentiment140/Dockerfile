FROM ubuntu:latest
MAINTAINER Oscar Araque

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists

VOLUME /input.txt
VOLUME /output.txt

CMD curl --data-binary @/input.txt "http://www.sentiment140.com/api/bulkClassify" > /output.txt
