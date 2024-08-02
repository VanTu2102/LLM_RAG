from langchain_model import langchain_huggingface_model
from typing import Optional
import chromadb
import numpy.typing as npt
import numpy as np
import chromadb.utils.embedding_functions as embedding_functions
from chromadb import Documents, EmbeddingFunction, Embeddings
import torch
from torch.nn.functional import normalize, pad

class CustomEmbeddingFunction(EmbeddingFunction):
    def __init__(
        self,
        model,
        tokenizer,
        vector_length: Optional[int] = 2048
    ):
        try:
            self._tokenizer = tokenizer
            self._model = model
            self._vector_length = vector_length
        except ImportError:
            raise ValueError(
                "The transformers and/or pytorch python package is not installed. Please install it with "
                "`pip install transformers` or `pip install torch`"
            )

    def __call__(self, input) -> Embeddings:
        embeddings = self._tokenizer(
            input, padding=True, truncation=True, return_tensors="pt"
        )
        return pad(normalize(embeddings["input_ids"].to(torch.float32), p=1.0), pad=(0, self._vector_length - embeddings["input_ids"].shape[1], 0, 0), mode='constant', value=0).numpy().tolist()


client = chromadb.Client()

collection = client.get_or_create_collection(
    name="vector_db",
    embedding_function=CustomEmbeddingFunction(langchain_huggingface_model.model, langchain_huggingface_model.tokenizer),
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
