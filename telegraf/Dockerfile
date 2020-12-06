FROM telegraf:1.16-alpine
RUN apk add --update \
    curl \
    openssl \
    python3 \
    py3-pip

RUN python3 -m pip install requests toml

CMD ["telegraf"]