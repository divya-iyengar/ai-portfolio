from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Chunk:
    chunk_id: int
    source: str
    text: str

@dataclass
class EmbeddedChunk:
    chunk_id: int
    source: str
    text: str
    embedding: list[float]

@dataclass
class RetrievedChunk:
    chunk_id: int
    source: str
    text: str
    similarity: float