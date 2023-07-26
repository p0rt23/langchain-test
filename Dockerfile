FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
  build-essential python3 python3-dev python3-pip gfortran curl openssl libssl-dev rust-all

#RUN apk update \
#  && apk --no-cache --update add \
#  build-base python3 python3-dev py3-pip gfortran curl openssl openssl-dev

# https://stackoverflow.com/questions/69684133/dl4006-warning-set-the-shell-option-o-pipefail-before-run-with-a-pipe-in-it
#SHELL ["/bin/ash", "-o", "pipefail", "-c"]
#RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
#ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app
COPY app .

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
  pip install -r requirements.txt --break-system-packages

CMD ["/usr/bin/python3", "app.py"]
