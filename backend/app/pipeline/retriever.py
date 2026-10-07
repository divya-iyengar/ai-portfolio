from app.pipeline import embedder
from app.pipeline.vector_store import VectorStore
from app.models.chunk import RetrievedChunk

store = VectorStore()

def retrieve(message):
    query_embedding = embedder.encode_query(message)
    raw_context = store.search(query_embedding=query_embedding, top_k=3)
    ids = raw_context["ids"][0]
    documents = raw_context["documents"][0]
    metadatas = raw_context["metadatas"][0]
    distances = raw_context["distances"][0]

    retrieved_chunks = []
    for id_, doc, meta, dist in zip(ids, documents, metadatas, distances):
        retrieved_chunks.append(RetrievedChunk(
            chunk_id=id_,
            source=meta["source"],
            text=doc,
            similarity=dist
        ))

    return retrieved_chunks


