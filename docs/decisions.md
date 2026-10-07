# Design Decisions

## Why RAG instead of fine-tuning?

The goal is to provide accurate responses about my background while allowing easy updates to the knowledge base.

RAG allows:
- updating information without retraining
- source attribution
- reduced hallucination risk

## Why vector database?

The goal is to use semantic retrieval instead of keyword search.

Vector database allows:
- user questions not matching exact wording
- embeddings capturing semantic similarity
- better for natural language queries

## Why FastAPI?

FastAPI provides:
- Python ecosystem compatibility
- simple API development
- compatibility with ML workflows

## Why ChromaDB?

Chosen for MVP because:
- local development simplicity 
- lightweight vector search
- easy migration to managed databases later

## Why defer agents?

The initial problem is knowledge retrieval, not autonomous decision making. 

Agentic workflows will be introduced for contexts where multi-step reasoning is required.