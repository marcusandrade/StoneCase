ARG DB_IMAGE

FROM ${DB_IMAGE}

WORKDIR /tmp
COPY ./initial_data/ .
RUN chmod +x /tmp/import.sh
ENTRYPOINT ["/tmp/import.sh"]
