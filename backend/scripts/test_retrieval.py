from app.pipeline.vector_store import VectorStore
from app.pipeline import embedder

store = VectorStore()
query = "What research experience does Divya have?"
query_embedding = embedder.encode_query(query)
results = store.search(
    query_embedding=query_embedding,
    top_k=3
)
print(results.keys())

for i in range(len(results["documents"][0])):
    print("-------------")
    print("SOURCE:")
    print(results["metadatas"][0][i])

    print("\nDISTANCE:")
    print(results["distances"][0][i])

    print("\nTEXT:")
    print(results["documents"][0][i])
