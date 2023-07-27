# langchain-test

## TODO
- Add Jenkinsfile to run on server, build image only.
- Discord bot
- What is a tokenizer?
- What is Seq2SeqLM?
- What is text2text-generation?
- What is a PromptTemplate?
- How to create custom data source

## Install

- [Quickstart doc for langchain](https://python.langchain.com/docs/get_started/quickstart.html)

For local LLM, it will download the model into the python cache directory.  It takes 50gb for
the FLAN-T5-XXL model, and it will need 50gb of memory as it loads all it all into RAM.  For
processing, it will use any many cores as is availabe.


```bash
sudo ./langchain-test

# Clear out pip cache which contains the local LLMs
sudo docker volume rm langchain-test-pip-cache
```
