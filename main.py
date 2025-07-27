from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    api_key="your-groq-api-key",
    model_name="llama3-70b-8192"
)

response = llm.invoke("Tell me a joke")
print(response)