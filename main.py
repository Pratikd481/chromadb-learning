from app.services.vector_store_service import VectorStoreService
from app.services.query_service import QueryService
import json

# service = VectorStoreService()

# result = service.query("Pc cheap")
# print(result)

query_service = QueryService()

for query in [
    "cheap mobile phone",
    "flagship premium laptop",
    "battery optimized smartwatch",
    "best headphones"
]:
    result = query_service.query(query, n=5)
    print("QUERY:", query)
    print(json.dumps(result, indent=2))
    
## Data Available:
# mobile
# laptop
# tablet
# smartwatch
# headphones
# camera
# Flagship premium device
# High performance device
# Budget friendly option
# Battery optimized device

