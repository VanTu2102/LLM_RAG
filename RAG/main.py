from vector_db import vector_db
from langchain_model import langchain_huggingface_model

# retriever
collection = vector_db.create_collection_cosine('vector_db', langchain_huggingface_model.model, langchain_huggingface_model.tokenizer)

