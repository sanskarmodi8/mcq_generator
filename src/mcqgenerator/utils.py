import PyPDF2
import re
from mcqgenerator.logger import logging

def extract_json(text):
    
    # Use regex to find the JSON part
    json_pattern = r'\{.*\}'
    try:
        match = re.search(json_pattern, text, re.DOTALL)
        return match.group(0)
    except Exception as e:
        print(e)
    


def read_file(file):
    text=""
    try:
        if file.name.endswith(".pdf"):
            pdf_reader = PyPDF2.PDFFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text+=page.extract_text()
                logging.info("loaded pdf file")
            return text
        elif file.name.endswith(".txt"):
            with open(file, "r") as f:
                text = f.read()
                logging.info("loaded txt file")
            return text
    except Exception as e:
        print(e)

def get_table_data(quiz:dict):
    try:
        quiz_table_data = []
        for key, value in quiz.items():
            mcq = value["mcq"]
            options = " | ".join([f"{option} : {option_value}" for option, option_value in value["options"].items()])
            correct = value["correct"]
            quiz_table_data.append({"MCQ":mcq, "Choices":options, "Correct":correct})
        logging.info("created tabular data from the result json")
        return quiz_table_data
    except Exception as e:
        print(e)