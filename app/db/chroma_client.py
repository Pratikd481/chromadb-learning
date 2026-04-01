import chromadb
from chromadb.config import Settings as ChromaSettings
from app.config import settings

class ChromaClient:
    def __init__(self):
        self.client = chromadb.Client(ChromaSettings( persist_directory=settings.CHROMA_PATH))
        

    def get_client(self):
        return self.client
    
    def persist(self):
        self.client.persist()