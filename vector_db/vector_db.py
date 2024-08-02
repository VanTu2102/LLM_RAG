import importlib
from typing import Optional
import chromadb
import numpy.typing as npt
import numpy as np
import chromadb.utils.embedding_functions as embedding_functions
from chromadb import Documents, EmbeddingFunction, Embeddings
from langchain_model import langchain_huggingface

class CustomEmbeddingFunction(EmbeddingFunction):
    def __init__(
        self,
        model: langchain_huggingface.model,
        tokenizer: langchain_huggingface.tokenizer
    ):
        try:
            self._torch = importlib.import_module("torch")
            self._tokenizer = tokenizer
            self._model = model
        except ImportError:
            raise ValueError(
                "The transformers and/or pytorch python package is not installed. Please install it with "
                "`pip install transformers` or `pip install torch`"
            )

    def __call__(self, input: Documents) -> Embeddings:
        embeddings = self._tokenizer(
            input, padding=True, truncation=True, return_tensors="pt"
        )
        return embeddings


client = chromadb.Client()

collection = client.get_or_create_collection(
    name="vector_db",
    embedding_function=CustomEmbeddingFunction(),
    metadata={"hnsw:space": "cosine"},
)
collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges",
    ],
    ids=["id1", "id2"],
)
results = collection.query(
    query_texts=[
        "This is a query document about hawaii"
    ],  # Chroma will embed this for you
    n_results=2,  # how many results to return
)
print(results)
