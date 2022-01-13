FROM openjdk:8

ARG ACTIVEMQ_VERSION
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION

ENV ACTIVEMQ_HOME /opt/activemq

RUN \
    curl -O http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-bin.tar.gz && \
    mkdir -p /opt && \
    tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ && \
    rm $ACTIVEMQ-bin.tar.gz && \
    ln -s /opt/$ACTIVEMQ $ACTIVEMQ_HOME && \
    useradd -r -M -d $ACTIVEMQ_HOME activemq && \
    chown activemq:activemq /opt/$ACTIVEMQ -R

RUN mkdir /opt/lib && \
    chown activemq:activemq /opt/lib -R

USER activemq

RUN curl -L https://github.com/j-white/activemq-k8s-discovery/releases/download/1.0.2/activemq-k8s-discovery-1.0.2-jar-with-dependencies.jar -o /opt/lib/activemq-k8s-discovery-1.0.2-jar-with-dependencies.jar

ENV ACTIVEMQ_USER_CLASSPATH /opt/lib

WORKDIR $ACTIVEMQ_HOME

EXPOSE 8161
EXPOSE 61616
EXPOSE 5672
EXPOSE 61613
EXPOSE 1883
EXPOSE 61614

CMD ["/bin/bash", "-c", "bin/activemq console"]