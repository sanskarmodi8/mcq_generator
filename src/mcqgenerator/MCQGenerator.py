import os
from dotenv import load_dotenv
import github_secrets.config
from langchain_ai21 import ChatAI21
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from mcqgenerator.logger import logging
import github_secrets


# load the env variables from .env file if available
# load_dotenv()

# set the environment variable
ai21_api_key = os.getenv("AI21_API_KEY")

if not ai21_api_key:
    raise ValueError("AI21_API_KEY environment variable is not set")

os.environ["AI21_API_KEY"] = ai21_api_key  # set the env var explicitly


# load the LLM
llm = ChatAI21(model="jamba-instruct")
logging.info("loaded ai21 llm thorugh langchain")

template = """
Text : {text}
You are an expert MCQ maker. Given the above, it is your job to create a quiz of {number} multiple choice \
questions for {subject} students in {tone} tone. Make sure the questions are not repeated and check all \
the questions to be confirming the text as well. Give your response exactly in the json format like RESPONSE_JSON below \
and use it as reference.  \
Ensure to make exactly {number} MCQs and give response in the same format as the RESPONSE_JSON. \
Given RESPONSE_JSON format :\
{response_json}
"""

# prompt for quiz generation 
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template
)

# llm chain for quiz generation
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

template2 = """
You are an expert English Grammarian and Writer. Given a multiple choice quiz for {subject} students. \
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use \
at max 50 words for the compelxity. If the quiz is not as per the cognitive and analytical abilities of \
the students, update the quiz questions which needs to be changed and change the tone such that it perfectly \
fits the students. \
Quiz MCQs:
{quiz}

Check the above quiz as an expert english writer.
"""

# prompt for quiz evaluation 
quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=template2)

# quiz evaluation chain 
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# combining the chains sequentially
chain = SequentialChain(chains=[quiz_chain,review_chain], 
                        input_variables=["text", "number", "subject", "tone", "response_json"],
                        output_variables=["quiz", "review"], verbose=True)
logging.info("loaded complete quiz generation chain")

