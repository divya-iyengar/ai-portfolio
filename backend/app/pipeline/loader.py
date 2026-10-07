from pathlib import Path

directory = Path('./knowledge_base')

def load():
    data = []

    for file in directory.rglob('*'):
        if file.is_file():
            try:
                content = file.read_text(encoding='utf-8')
            except (UnicodeDecodeError, PermissionError, FileNotFoundError):
                content = "[Unreadable or Binary Content]"
        
            data.append({
                'file': file.name,
                'content': content
            })

    return {"response": data}