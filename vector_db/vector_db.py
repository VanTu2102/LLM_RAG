from typing import Optional
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import torch
from torch.nn.functional import normalize, pad


class CustomEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model, tokenizer, vector_length: Optional[int] = 2048):
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
        return (
            pad(
                normalize(embeddings["input_ids"].to(torch.float32), p=1.0),
                pad=(0, self._vector_length - embeddings["input_ids"].shape[1], 0, 0),
                mode="constant",
                value=0,
            )
            .numpy()
            .tolist()
        )


client = chromadb.Client()


def create_collection_cosine(name, model, tokenizer, vector_length: Optional[int] = 2048):
    return client.get_or_create_collection(
        name=name,
        embedding_function=CustomEmbeddingFunction(model, tokenizer, vector_length),
        metadata={"hnsw:space": "cosine"},
    )