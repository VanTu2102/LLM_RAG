import getpass
import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "sk-proj-PvEuxmAlrEx6gAeXuTORT3BlbkFJYHP8DZGLgPfEy8tZXOlu"

model = ChatOpenAI(model="gpt-3.5-turbo-1106")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

print(model.invoke(messages).content)