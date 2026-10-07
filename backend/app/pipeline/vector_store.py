from __future__ import annotations
import chromadb
from app.models.chunk import EmbeddedChunk


class VectorStore:

    def __init__(self, path="vector_db"):
        self.client = chromadb.PersistentClient(path=path)

        self.collection = self.client.get_or_create_collection(name="porfolio_knowledge")

    def store(self, chunks: list[EmbeddedChunk]):
        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for chunk in chunks:
            ids.append(str(chunk.chunk_id))
            embeddings.append(chunk.embedding)
            documents.append(chunk.text)

            metadatas.append({
                "source": chunk.source,
                "chunk_id": chunk.chunk_id
            })

            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas
            )

    def search(self, query_embedding, top_k):
        results = self.collection.query(query_embeddings=[query_embedding], n_results=top_k)
        return results