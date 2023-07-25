FROM alpine:3 as python-build

RUN apk update \
  && apk --no-cache --update add \
  build-base python3 python3-dev py3-pip gfortran

WORKDIR /app
COPY app .

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
  pip install -r requirements.txt

CMD ["/usr/bin/python3", "app.py"]
