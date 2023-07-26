#!/usr/bin/python3

import sys
from dotenv import load_dotenv
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

# HUGGINGFACEHUB_API_TOKEN 
load_dotenv()

# https://www.packtpub.com/article-hub/making-the-best-out-of-hugging-face-hub-using-langchain

repo_id = "databricks/dolly-v2-3b"
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0, "max_length":128})
 
template = """Question: {question}
 
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

while True:
    question = input("Your question (exit to quit): ")

    if question == "exit":
        sys.exit()
    else:
        print(llm_chain.run(question))
