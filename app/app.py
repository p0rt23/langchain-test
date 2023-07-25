#!/usr/bin/python3

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

# question = "In the first movie of Harry Potter, what is the name of the three-headed dog?"
question = "What is the best way to eat a banana?"

print(llm_chain.run(question))
