FROM alpine:3 as python-build

RUN apk update \
  && apk --no-cache --update add \
  build-base python3 python3-dev py3-pip gfortran

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir python-dotenv
RUN pip install --no-cache-dir langchain
RUN pip install --no-cache-dir huggingface_hub

WORKDIR /app
COPY app .

CMD ["/usr/bin/python3", "app.py"]
