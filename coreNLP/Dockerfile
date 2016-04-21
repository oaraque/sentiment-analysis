FROM java:8-jre-alpine
MAINTAINER Oscar Araque

RUN mkdir /corenlp
WORKDIR /corenlp

RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip
RUN unzip *.zip && rm *.zip

ENV JAVA_OPTS -Xmx2g

VOLUME /input.txt
VOLUME /input.txt.out
VOLUME /corenlp/props.properties

CMD java -cp "./stanford-corenlp-full-2015-12-09/*" $JAVA_OPTS edu.stanford.nlp.pipeline.StanfordCoreNLP -props props.properties
