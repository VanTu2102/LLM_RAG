from vector_db import vector_db
from langchain_model import langchain_huggingface_model

# retriever
collection = vector_db.create_collection_cosine('vector_db', langchain_huggingface_model.model, langchain_huggingface_model.tokenizer)
collection.add(
    documents=[
        "This is a document about the fruit as pineapple and orange",
        "This is a document about the country as VietNam, Chinese. Vietnam and China have deep historical ties, complex political relations, and significant trade connections."
    ],
    ids=["id1", "id2"],
)

#promt and get document
query = "This is a query about the VietNam and Chinesse"
results = collection.query(
    query_texts=[
        query
    ],
    n_results=1
)

# Generator
prompt = f"document: '{results['documents'][0][0]}',Can you make the paragraph about content of document?"
inputs = langchain_huggingface_model.tokenizer(prompt, return_tensors="pt")
generate_ids = langchain_huggingface_model.model.generate(inputs.input_ids, max_length=300)
print(langchain_huggingface_model.tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])