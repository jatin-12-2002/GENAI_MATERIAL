import json
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from MCQGenerator.utils import read_file,get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from MCQGenerator.MCQGenerator import generate_evaluate_chain

#loading json file
with open('/workspaces/Automated_MCQ_Generator/Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

#print(RESPONSE_JSON)