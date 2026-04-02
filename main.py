from app.services.vector_store_service import VectorStoreService

service = VectorStoreService()

# simulate usage
service.add_documents(["hello world Tesst"], ["2"])

result = service.query("hello")
print(result)