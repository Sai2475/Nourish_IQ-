from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    api_key="",
    model_name="llama3-70b-8192-verstaile"
    temperature = 0.0
)

prompt_template_resto = PromptTemplate(
    input_variables=['age','gender','weight','height','veg_or_nonveg','disease','region','foodtype'],
    template=(
        
    )
)