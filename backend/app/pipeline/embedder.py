from sentence_transformers import SentenceTransformer
from app.models.chunk import EmbeddedChunk

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def encode_query(query):
    return model.encode(query)


def process(chunks, batch_size=32):
    embedded_chunks = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        texts = [chunk.text for chunk in batch]
        embeddings = model.encode(texts)
        for chunk, embedding in zip(batch, embeddings):
            embedded_chunks.append(EmbeddedChunk(
                chunk_id = chunk.chunk_id,
                source = chunk.source,
                text = chunk.text,
                embedding = embedding
            ))

    return embedded_chunks