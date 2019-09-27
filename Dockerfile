FROM alpine:3.10

COPY LICENSE README.md entrypoint.sh /

COPY src/create-file.py /create-file.py

RUN apk add python3

ENTRYPOINT ["/entrypoint.sh"]
