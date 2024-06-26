import gradio as gr
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

from langchain_core.messages import HumanMessage, SystemMessage,AIMessage

import os

chat=ChatGroq(groq_api_key=os.environ['GROQ_API_KEY'], model_name="mixtral-8x7b-32768")


def predict(message, history):
    history_lst = []
    history_lst.append(SystemMessage(content="You are a helpful assistant called Jarvis, specialized in data science and machine learning"))
    for human, ai in history:
        history_lst.append(HumanMessage(content=human))
        history_lst.append(AIMessage(content=ai))
    history_lst.append(HumanMessage(content=message))
    ans = chat(history_lst)
    return ans.content

gr.ChatInterface(predict,
                title="Jarvis ChatBot",
                description="Alternative to chatGPT, this chatbot use Mixtral-8x7B-32768 model with higher processing speeds and response",
                theme="HaleyCH/HaleyCH_Theme",).launch()