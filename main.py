from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os

llm_resto = ChatGroq(
    api_key="",
    model_name="llama3-70b-8192-verstaile"
    temperature = 0.0
)

prompt_template_resto = PromptTemplate(
    input_variables=['age','gender','weight','height','veg_or_nonveg','disease','region','foodtype'],
    template=(
        "Diet Recommendation System:\n"
        "I want you to provide output in the following format using the input criteria:\n\n"
        "Restaurants:\n"
        "- name1\n- name2\n- name3\n- name4\n- name5\n- name6\n\n"
        "Breakfast:\n"
        "- item1\n- item2\n- item3\n- item4\n- item5\n- item6\n\n"
        "Dinner:\n"
        "- item1\n- item2\n- item3\n- item4\n- item5\n\n"
        "Workouts:\n"
        "- workout1\n- workout2\n- workout3\n- workout4\n- workout5\n- workout6\n\n"
        "Criteria:\n"
        "Age: {age}, Gender: {gender}, Weight: {weight} kg, Height: {height} ft, "
        "Vegetarian: {veg_or_nonveg}, Disease: {disease}, Region: {region}, "
        "Allergics: {allergics}, Food Preference: {foodtype}.\n"

 )
)

chain = LLMChain(llm = llm_resto, prompt = prompt_template_resto)