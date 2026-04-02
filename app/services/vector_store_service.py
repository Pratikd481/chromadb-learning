from app.db.collection_manager import CollectionManager
from app.db.chroma_client import ChromaClient

class VectorStoreService:
    def __init__(self):
        self.collection = CollectionManager().getCollection()
        self.client = ChromaClient().get_client()
        
    def add_documents(self, docs, ids):
        self.collection.add(documents=docs, ids=ids)
        print(f"Collection count: {self.collection.count()}")

    def query(self, query_text, n=3):
        return self.collection.query(
            query_texts=[query_text],
            n_results=n
            #include=["embeddings", "documents", "distances"]
        )