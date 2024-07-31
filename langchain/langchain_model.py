import getpass
import os

# from langchain_openai import chat_models
# from langchain import llms

# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = "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"
# os.environ["OPENAI_API_KEY"] = "sk-proj-OD1PVkNfYWOuVcXtbjFvT3BlbkFJVNuE1NaQIp441LPAwX0t"

# # model = chat_models.ChatOpenAI(model="gpt-4o-mini")
# model = llms
# messages = [
#     (
#         "system",
#         "You are a helpful translator. Translate the user sentence to French.",
#     ),
#     ("human", "I love programming."),
# ]
# print(model.invoke(messages))

import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3.1-8B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print(output)