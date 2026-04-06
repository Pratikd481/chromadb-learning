import hashlib
from datetime import datetime
import json
from app.db.chroma_client import ChromaClient
from app.config import settings

class IngestionService:
    def __init__(self):
        self.client = ChromaClient().get_client()
        
        self.collection = self.client.get_or_create_collection(
            name=settings.PRODUCT_COLLECTION_NAME
        )
        
        
    # -----------------------------
    # ID GENERATION (DETERMINISTIC)
    # -----------------------------
    def _generate_versioned_id(self, product_id, version) :
        return f"{product_id}_v{version}"
    
    
    # --------------------------------------
    # INTERNAL: BUILD DOCUMENT STRING
    # --------------------------------------
    def _build_document(self, item):
        return f"""
        Product: {item['name']}
        Description: {item['description']}
        Category: {item['category']}
        Price: {item['price']}
        """
        
    # -----------------------------
    # INSERT NEW PRODUCT (WITH VERSIONING)
    # -----------------------------
    def insert_product(self, product_id, product):
        # Check existing versions to determine next version
        existing_results = self.collection.get(
            ids=[product_id],
            where={"product_id": product_id}
        )
        
        if existing_results['ids']:
            # Product exists, get max version and increment
            existing_metadatas = existing_results['metadatas']
            max_version = max(meta['version'] for meta in existing_metadatas)
            version = max_version + 1
            
            # Mark all previous versions as inactive
            for meta in existing_metadatas:
                if meta['is_active']:
                    # Note: ChromaDB doesn't support direct metadata updates on existing items
                    # You'd need to re-add with updated metadata or use a different approach
                    pass  # Placeholder - see note below
        else:
            version = 1
        
        document = self._build_document(product)
        
        # Use upsert for atomic insert/update
        self.collection.upsert(
            ids=[product_id],
            documents=[document],
            metadatas=[{
                "product_id": product_id,
                "version": version,
                "is_active": True,
                "updated_at": datetime.now().isoformat()
            }]
        )
        print(f"Inserted/Updated product {product_id} version {version}")
        
    def ingest_file(self, file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        
        for item in data:
            self.insert_product(item["product_id"], item)
            
        print("File ingestion complete")