from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Folder containing resumes
resume_folder = "resumes"

documents = []
file_names = []

# Read all resume files
for file in os.listdir(resume_folder):
    if file.endswith(".txt"):
        file_path = os.path.join(resume_folder, file)

        with open(file_path, "r", encoding="utf-8") as f:
            documents.append(f.read())
            file_names.append(file)

# Convert resumes into embeddings
embeddings = model.encode(documents)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Store embeddings
index.add(embeddings)

# Save index
faiss.write_index(index, "resume_index.faiss")

# Save filenames
with open("resume_files.pkl", "wb") as f:
    pickle.dump(file_names, f)

print("✅ Resume embeddings created successfully!")