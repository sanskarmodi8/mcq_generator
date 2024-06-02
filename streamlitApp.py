import json
import streamlit as st
import pandas as pd
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data, extract_json
from src.mcqgenerator.MCQGenerator import chain

response_json=""

# json response format
response_json = {
    "1" : {
        "mcq" : "multiple choice question",
        "options" : {
            "a" : "choice here",
            "b" : "choice here",
            "c" : "choice here",
            "d" : "choice here",
        },
        "correct" : "correct answer",
    } ,
    "2" : {
        "mcq" : "multiple choice question",
        "options" : {
            "a" : "choice here",
            "b" : "choice here",
            "c" : "choice here",
            "d" : "choice here",
        },
        "correct" : "correct answer",
    } ,
    "3" : {
        "mcq" : "multiple choice question",
        "options" : {
            "a" : "choice here",
            "b" : "choice here",
            "c" : "choice here",
            "d" : "choice here",
        },
        "correct" : "correct answer",
    } ,
}
    
# streamlit app title
st.title("MCQ Generator using Langchain")

# form for user inputs
with st.form("user_unputs"):
    uploaded_file = st.file_uploader("Upload a PDF or TXT File")
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
    subject = st.text_input("Enter Subject", max_chars=20)
    tone = st.text_input("Complexity level of questions", max_chars=20, placeholder="Basic/Medium/Advanced")
    btn = st.form_submit_button("Generate MCQs")
    
    if btn and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Generating..."):
            try:
                text=read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response = chain(
                                {
                                "text": text,
                                "number": mcq_count,
                                "subject": subject,
                                "tone" : tone,
                                "response_json" : json.dumps(response_json)
                                }
                            )
                    print(response.get("quiz"))
                    extracted_json = extract_json(response.get("quiz"))
                    print()
                    print(extracted_json)
                    print()
                    quiz = json.loads(extracted_json)
                    print()
                    print(quiz)
                    print()
                    table = get_table_data(quiz)
                    print()
                    print(table)
                    print()
                    df = pd.DataFrame(table)
                    print()
                    print(df)
                    print()
                    df.to_csv("mcqs.csv")
                    df.index=df.index+1
                    print()
                    print(df)
                    print()
                    st.dataframe(df)
                    st.text_area(label="Review", value=response["review"])
                    
            except Exception as e:
                print(e)
                
            

