

def construct(message, chunks):
    prompt = """You are an AI assistant that answers questions about Divya Iyengar's career - work experiences, aspirations, research and background. \n
    Answer using the retrieved context as primary evidence. When the user's question refers to a related role, skill, or concept (for example, customer-facing engineering vs. Forward Deployed Engineering), synthesize the available evidence to explain the relationship. Do not invent experience that is unsupported.\n
    But in terms of evidence, use ONLY the provided context. If the answer isn't accurate based on the context, say you don't know.\n
    Context: \n\n"""
    
    for i, chunk in enumerate(chunks, start=1):
        prompt += f"Source {i}: {chunk.source}\n"
        prompt += f"{chunk.text}\n\n"
    
    prompt += f"Question:\n{message}"

    return prompt

