import os

class Settings:
    CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_data")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "documents")

settings = Settings()
# print(f"Chroma Path: {settings.CHROMA_PATH}")
# print(f"Collection Name: {settings.COLLECTION_NAME}")