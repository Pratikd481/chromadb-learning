from app.db.collection_manager import CollectionManager
from app.db.chroma_client import ChromaClient

class VectorStoreService:
    def __init__(self):
        self.collection = CollectionManager().getCollection()
        self.chroma_client = ChromaClient().get_client()
        
    def add_documents(self, documents):
        self.collection.add(documents)
        self.chroma_client.persist()
        
    def query(self, query, n_results=5):
        results = self.collection.query(query_texts=[query], n_results=n_results)
        return results