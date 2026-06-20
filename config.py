from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))

    COLLECTION_NAME = os.getenv(
        "COLLECTION_NAME",
        "system_design_books"
    )

    EMBED_MODEL = os.getenv(
        "EMBED_MODEL",
        "BAAI/bge-small-en-v1.5"
    )

    CHUNK_SIZE = int(
        os.getenv("CHUNK_SIZE", 800)
    )

    CHUNK_OVERLAP = int(
        os.getenv("CHUNK_OVERLAP", 100)
    )

    TOP_K = int(
        os.getenv("TOP_K", 10)
    )

    OCR_ENABLED = (
        os.getenv("OCR_ENABLED", "true").lower()
        == "true"
    )
    
    GROQ_MODEL = os.getenv(
        "GROQ_MODEL",
        "llama-3.3-70b-versatile"
        )


settings = Settings()