import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("resume_index.faiss")

# Load filenames
with open("resume_files.pkl", "rb") as f:
    file_names = pickle.load(f)

def retrieve_resume(query):

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    D, I = index.search(query_embedding, 1)

    best_match = file_names[I[0][0]]

    with open(f"resumes/{best_match}", "r", encoding="utf-8") as f:
        return f.read()


# Test

if __name__ == "__main__":

    q = input("Search Resume : ")

    result = retrieve_resume(q)

    print(result)