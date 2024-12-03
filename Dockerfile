FROM apache/kafka:latest

ARG LOG_PATH=/tmp/kafka/logs
RUN mkdir -p $LOG_PATH && \
    chmod -R 755 $LOG_PATH
