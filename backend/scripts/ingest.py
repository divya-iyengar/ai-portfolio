from app.pipeline import loader, chunker, embedder
from app.pipeline.vector_store import VectorStore
import json

print("Loading documents...")
json_data = loader.load()
if json_data:
    file_data = json_data.get("response", [])
    print(f"Loaded {len(file_data)} files!")

    print("Chunking...")
    chunks = chunker.process(file_data)
    print(f"Created {len(chunks)} chunks!")

    print("Generating embeddings...")
    embedded_chunks = embedder.process(chunks)
    print("Finished.")

    vector_store = VectorStore()
    print("Persisting vector database...")
    vector_store.store(embedded_chunks)
    print("Done.")

    print("Ingestion complete!")






