from app.db.chroma_client import ChromaClient
from app.config import settings


class QueryService:
    def __init__(self):
        self.client = ChromaClient().get_client()
        
        self.collection = self.client.get_or_create_collection(
            name=settings.PRODUCT_COLLECTION_NAME
        )
        
    def query(self, query_text, n=3):
        return self.collection.query(
            query_texts=[query_text],
            n_results=n
        )
        