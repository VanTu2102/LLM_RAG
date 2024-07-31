import getpass
import os

from langchain_openai import chat_models
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "sk-proj-MHpGTFRaPeNFTaEaGWHFT3BlbkFJABUMjlLmcKTWa5th45rm"

model = chat_models.ChatOpenAI(model="gpt-4")
messages = [
    (
        "system",
        "You are a helpful translator. Translate the user sentence to French.",
    ),
    ("human", "I love programming."),
]
print(model.invoke(messages))