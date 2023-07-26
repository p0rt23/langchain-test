FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
  build-essential python3 python3-dev python3-pip gfortran curl openssl libssl-dev rust-all

WORKDIR /app
COPY app .

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
  pip install -r requirements.txt --break-system-packages

CMD ["/usr/bin/python3", "app.py"]
