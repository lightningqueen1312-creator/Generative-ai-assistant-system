import os

# ===========================
# Base Directory
# ===========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ===========================
# Project Folders
# ===========================

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")
CHAT_HISTORY_PATH = os.path.join(BASE_DIR, "chat_history")
DATA_FOLDER = os.path.join(BASE_DIR, "data")
DOCUMENT_FOLDER = os.path.join(DATA_FOLDER, "documents")

# ===========================
# Chunk Settings
# ===========================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ===========================
# Embedding Model
# ===========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===========================
# Gemini Model
# ===========================

LLM_MODEL = "gemini-2.5-flash"

# ===========================
# Retrieval Settings
# ===========================

TOP_K = 4

# ===========================
# Create Required Folders
# ===========================

folders = [
    UPLOAD_FOLDER,
    VECTOR_DB_PATH,
    CHAT_HISTORY_PATH,
    DATA_FOLDER,
    DOCUMENT_FOLDER,
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)