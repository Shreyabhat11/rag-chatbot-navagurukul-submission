from embeddings.embedder import Embedder
from vectordb.qdrant_manager import (
    QdrantManager
)


class Retriever:

    def __init__(self):

        self.embedder = Embedder()

        self.qdrant = QdrantManager()

    def retrieve(
        self,
        query,
        top_k=50
    ):

        query_embedding = (
            self.embedder.embed_text(
                query
            )
        )

        results = self.qdrant.search(
            query_embedding,
            limit=top_k
        )

        chunks = []

        for result in results:

            chunks.append({

                "score":
                    result.score,

                "pdf_name":
                    result.payload[
                        "pdf_name"
                    ],

                "page_number":
                    result.payload[
                        "page_number"
                    ],

                "text":
                    result.payload[
                        "text"
                    ]
            })

        return chunks