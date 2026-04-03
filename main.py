from app.services.vector_store_service import VectorStoreService

service = VectorStoreService()

# simulate usage
service.add_documents(["Mobile under 50k"], ["5"])
service.add_documents(["Mobile under 20k"], ["6"])
service.add_documents(["Tablet under 20k"], ["7"])
service.add_documents(["Tablet under 20k"], ["8"])
service.add_documents(["Laptop under 20k"], ["9"])
result = service.query("Pc cheap")
print(result)