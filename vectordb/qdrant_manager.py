from qdrant_client import QdrantClient

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from config import settings


class QdrantManager:

    def __init__(self):

        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )
        print(type(self.client))
        print(dir(self.client))

    def create_collection(
        self,
        vector_size: int
    ):

        collections = self.client.get_collections()

        existing = [
            c.name
            for c in collections.collections
        ]

        if settings.COLLECTION_NAME in existing:

            print(
                "Collection already exists."
            )

            return

        self.client.create_collection(
            collection_name=
            settings.COLLECTION_NAME,

            vectors_config=
            VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

        print(
            "Collection created."
        )

    def insert_chunks(
        self,
        chunks,
        embeddings
    ):

        points = []

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):

            points.append(

                PointStruct(

                    id=chunk["chunk_id"],

                    vector=embedding,

                    payload={

                        "pdf_name":
                            chunk["pdf_name"],

                        "page_number":
                            chunk["page_number"],

                        "chunk_index":
                            chunk["chunk_index"],

                        "text":
                            chunk["text"]
                    }
                )
            )

        self.client.upsert(
            collection_name=
            settings.COLLECTION_NAME,

            points=points
        )

        print(
            f"Inserted {len(points)} chunks"
        )

    def count(self):

        result = self.client.count(
            collection_name=
            settings.COLLECTION_NAME
        )

        return result.count
    
    def search(self,query_vector,limit=20):

        results = self.client.query_points(
            collection_name=settings.COLLECTION_NAME,
            query=query_vector,
            limit=limit,
            with_payload=True
        )

        return results.points