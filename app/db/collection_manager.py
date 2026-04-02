from app.db.chroma_client import ChromaClient
from app.config import settings

class CollectionManager:
    def __init__(self):
        self.client = ChromaClient().get_client()
        self.collection = self.client.get_or_create_collection(settings.COLLECTION_NAME)   
        
    def getCollection(self):
        return self.collection