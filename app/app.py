import sys
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_id = "google/flan-t5-large" 
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

llm = HuggingFacePipeline(pipeline = pipeline(
    "text2text-generation",
    model = model,
    tokenizer = tokenizer,
    max_length = 100
))
 
template = """Question: {question}
 
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

while True:
    question = input("Your question (\"q\" to quit): ")

    if question == "q":
        sys.exit()
    else:
        print(llm_chain.run(question))
