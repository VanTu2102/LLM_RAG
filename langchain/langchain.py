import getpass
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "sk-None-yRdDXOeUslynDkzNZQUmT3BlbkFJKrcvPdOgEhPVhuTYESD0"

from langchain_openai import chat_models
import langchain

model = chat_models.ChatOpenAI(model="gpt-4")