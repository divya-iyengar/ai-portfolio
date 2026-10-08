from app.pipeline import retriever, prompt_builder
from app.pipeline.llm_client import LLMClient
from app.models.chat import ChatResponse

client = LLMClient()

def generate_response(message):
    print("CHAT SERVICE START", flush=True)
    chunks = retriever.retrieve(message)
    prompt = prompt_builder.construct(message, chunks)
    answer = client.generate(prompt)
    return ChatResponse(
        answer=answer,
        sources=[chunk.source for chunk in chunks]
    )