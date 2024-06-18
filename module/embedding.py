import json
import torch
from typing import List, Dict
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


def load_sbert_model(model_name: str) -> Dict:
    model = SentenceTransformer(model_name)
    if torch.cuda.is_available():
        model = model.to(torch.device("cuda"))
    # print(f"Loaded SBERT model: {model_name}")
    # print(model.device
    return {"model": model}


def encode_text(texts: List[str], model_name: str, batch_size: int = 16) -> np.ndarray:
    encoded_texts = []
    model = load_sbert_model(model_name)
    # print(type(model["model"]))
    for i in range(0, len(texts), batch_size):
        # print(texts[i:i + batch_size])
        encoded_texts.append(model["model"].encode(texts[i:i + batch_size]))
    return np.concatenate(encoded_texts, axis=0)


def index_texts(path,encoded_texts: np.ndarray, n_dimensions: int, n_centroids: int, model_name: str) -> None:
    index = faiss.IndexFlatL2(n_dimensions)  
    index.add(encoded_texts)
    faiss.write_index(index, path)


def index_texts_with_sbert(texts: List[str], model_name: str,path: str, batch_size: int = 16, n_centroids: int = 1000) -> None:
    # print(type(texts))
    encoded_texts = encode_text(texts, model_name, batch_size=batch_size)
    n_dimensions = encoded_texts.shape[1]
    index_texts(path,encoded_texts, n_dimensions, n_centroids, model_name)


if __name__ == "__main__":
    # texts = ["This function is used to create a new category. It takes a CategoryDTO object as an input parameter
    # and returns a Result<String> object as an output parameter.", "This function is used to query a page of
    # categories. It takes a CategoryPageQueryDTO object as an input parameter and returns a Result<PageResult>
    # object as an output parameter.", "This function is used to delete a category ry by its id. It takes a Long id as
    # an input parameter and returns a Result<String> object as an output parameter.", "This function is used to
    # update a category. It takes a CategoryDTO object as an input parameter and returns a Result<String> object as
    # an output parameter.", "This function is used to enable or disable a category. It takes an Integer status and a
    # Long id as input parameters and returns a Result<String> object as an output parameter.", "This function is
    # used to query a list of categories by type. It takes an Integer type as an input parameter and returns a
    # Result<List<Category>> object as an output parameter.",] model_name = "distiluse-base-multilingual-cased-v2"
    texts = list(json.load(open("save.json")).values())
    index_texts_with_sbert(texts, "multi-qa-mpnet-base-cos-v1","file_save.index")
    faiss_index = faiss.read_index("file_save.index")
    # print(faiss_index.ntotal)
    query = "update the setmeal"
    query_embedding = encode_text([query], load_sbert_model("multi-qa-mpnet-base-cos-v1"))
    # print(query_embedding.shape)
    # print(faiss_index.search(np.expand_dims(query_embedding, axis=0), 10))
    distances, indices = faiss_index.search(query_embedding, 10)
    for i in range(len(indices[0])):
        text = texts[indices[0][i]]
        print(f'Top {i + 1}: {text}, Distance: {distances[0][i]}')
