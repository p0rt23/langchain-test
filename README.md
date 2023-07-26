# langchain-test

## TODO
- How to use local resources / services vs API calls
- How to create custom data source

## Install

Need to create a [.env](https://pypi.org/project/python-dotenv/) file in ./app/ with 
HUGGINGFACEHUB_API_TOKEN defined.

- [Quickstart doc for langchain](https://python.langchain.com/docs/get_started/quickstart.html)

```bash
sudo docker build . -t p0rt23/langchain-test
sudo docker run --rm -it -v langchain-test-pip-cache:/root/.cache p0rt23/langchain-test
```
