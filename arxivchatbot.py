import os
import gradio as gr
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import AgentType, initialize_agent
from langchain.tools import ArxivQueryRun
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage

# Load environment variables
load_dotenv()

# Initialize the ChatGroq model
chat = ChatGroq(groq_api_key=os.environ['GROQ_API_KEY'], model_name="mixtral-8x7b-32768")

# Initialize the ArXiv tool
arxiv_tool = ArxivQueryRun()
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

# Initialize conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the agent
agent = initialize_agent(
    [arxiv_tool,wiki],
    chat,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    system_message=SystemMessage(content="You are Jarvis, an AI assistant specialized in querying the arXiv and Wikipedia database for scientific papers. Always use the ArxivQueryRun tool to search for papers when asked about scientific topics and and WikipediaQueryRun for everything else that you didn't find in arxiv.")
)

def predict(message, history):
    # Format the history for the agent
    formatted_history = []
    for human, ai in history:
        formatted_history.append(f"Human: {human}")
        formatted_history.append(f"AI: {ai}")
    
    # Add the new message
    formatted_history.append(f"Human: {message}")
    
    # Get the response from the agent
    response = agent.run("\n".join(formatted_history))
    
    return response

# Create and launch the Gradio interface
demo = gr.ChatInterface(
    predict,
    title="Jarvis AI",
    description="AI assistant specialized in querying the arXiv and Wikipedia database for scientific as well as general purpose information.")
demo.launch()