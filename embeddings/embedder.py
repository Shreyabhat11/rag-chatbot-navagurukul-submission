from sentence_transformers import SentenceTransformer
from config import settings


class Embedder:

    def __init__(self):

        print(
            f"Loading embedding model: "
            f"{settings.EMBED_MODEL}"
        )

        self.model = SentenceTransformer(
            settings.EMBED_MODEL
        )

    def embed_text(self, text: str):

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def embed_batch(
        self,
        texts: list[str]
    ):

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        return embeddings.tolist()

    def get_dimension(self):

        return self.model.get_sentence_embedding_dimension()