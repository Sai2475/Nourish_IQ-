from flask import Flask, render_template, request
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)