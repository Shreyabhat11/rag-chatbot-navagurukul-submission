from vectordb.qdrant_manager import (
    QdrantManager
)

q = QdrantManager()

print(
    "Stored vectors:",
    q.count()
)