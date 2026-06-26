from sentence_transformers import SentenceTransformer

# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """
    embeddings = model.encode(chunks, convert_to_numpy=True)

    return embeddings


def embed_query(query):
    """
    Generate embedding for a user query.
    """
    return model.encode(query, convert_to_numpy=True)