from app.pipeline import retriever, prompt_builder
from app.pipeline.llm_client import LLMClient
from app.models.chat import ChatResponse

client = LLMClient()

def generate_response(message):
    print("CHAT SERVICE START", flush=True)
    chunks = retriever.retrieve(message)
    print("2: RETRIEVAL COMPLETE", flush=True)
    prompt = prompt_builder.construct(message, chunks)
    print("3: PROMPT BUILT", flush=True)
    answer = client.generate(prompt)
    print("4: LLM COMPLETE", flush=True)
    return ChatResponse(
        answer=answer,
        sources=[chunk.source for chunk in chunks]
    )