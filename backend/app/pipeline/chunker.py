from app.models.chunk import Chunk
chunk_size = 500
chunk_overlap = 100
search_window = 100
sentence_endings = [". ", "! ", "? "]

def process(data):
    chunks = []
    for file_data in data:
        if file_data:
            source = file_data.get("file")
            content = file_data.get("content")
            curr_chunks = len(chunks)
            chunks.extend(chunk(source, content, curr_chunks))
    
    return chunks

def chunk(source, content, curr_chunks):
    id_num = curr_chunks
    file_chunks = []
    while len(content) > chunk_size:
        char_idx = determine_best_split(content)
        file_chunks.append(Chunk(
            chunk_id=id_num,
            source=source,
            text=content[:char_idx]
        ))
        content = content[char_idx:]
        id_num+=1
    if len(content) <= chunk_size:
        file_chunks.append(Chunk(
            chunk_id=id_num,
            source=source,
            text=content
        ))
    return file_chunks

def determine_best_split(content):
    left = content[:chunk_size]
    left_idx = [-1, -1, -1, -1]
    left_idx[0] = left.rfind("\n\n")
    left_idx[1] = left.rfind("\n")
    sentence_rindices = [left.rfind(e) for e in sentence_endings if left.rfind(e) != -1]
    left_idx[2] = max(sentence_rindices) if sentence_rindices else -1
    left_idx[3] = left.rfind(", ")
    char_index = len(left)-1
    priority = 4
    for i, value in enumerate(left_idx):
        difference = abs(value - chunk_size)
        if difference <= search_window:
            char_index = value
            priority = i
            break
    right = content[chunk_size:]
    if right:
        right_idx = [-1, -1, -1, -1]
        right_idx[0] = right.find("\n\n")
        right_idx[1] = right.find("\n")
        sentence_indices = [right.find(e) for e in sentence_endings if right.find(e) != -1]
        right_idx[2] = min(sentence_indices) if sentence_indices else -1
        right_idx[3] = right.find(", ")
        right_index = 0
        right_priority = 4
        for i, value in enumerate(right_idx):
            if value <= search_window and value >= 0:
                right_index = value
                right_priority = i
                break
        if right_priority <= priority:
            char_index = right_index + chunk_size
    return char_index
    