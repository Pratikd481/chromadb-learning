import chromadb
from app.config import settings

class ChromaClient:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_PATH)
        

    def get_client(self):
        return self.client