import faiss
import numpy as np
import pickle
import os

INDEX_FILE = "vector_db/faiss_index.bin"
CHUNKS_FILE = "vector_db/chunks.pkl"


def save_vector_store(embeddings, chunks):
    """
    Save embeddings and corresponding text chunks.
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    os.makedirs("vector_db", exist_ok=True)

    faiss.write_index(index, INDEX_FILE)

    with open(CHUNKS_FILE, "wb") as f:
        pickle.dump(chunks, f)


def load_vector_store():
    """
    Load FAISS index and text chunks.
    """

    index = faiss.read_index(INDEX_FILE)

    with open(CHUNKS_FILE, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def search_similar_chunks(query_embedding, top_k=3):
    """
    Search the most relevant chunks.
    """

    index, chunks = load_vector_store()

    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results