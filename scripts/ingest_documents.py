from pathlib import Path
from tqdm import tqdm

from ingestion.pdf_parser import PDFParser
from ingestion.chunker import Chunker

from embeddings.embedder import Embedder
from vectordb.qdrant_manager import QdrantManager


PDF_FOLDER = "data/pdfs"
BATCH_SIZE = 128


def process_chunks(
    chunks,
    embedder,
    qdrant
):

    for i in range(
        0,
        len(chunks),
        BATCH_SIZE
    ):

        batch = chunks[i:i+BATCH_SIZE]

        texts = [
            c["text"]
            for c in batch
        ]

        embeddings = embedder.embed_batch(
            texts
        )

        qdrant.insert_chunks(
            batch,
            embeddings
        )


def main():

    parser = PDFParser()

    chunker = Chunker()

    embedder = Embedder()

    qdrant = QdrantManager()

    vector_dim = (
        embedder.get_dimension()
    )

    qdrant.create_collection(
        vector_dim
    )

    pdf_files = list(
        Path(PDF_FOLDER).glob("*.pdf")
    )

    print(
        f"Found {len(pdf_files)} PDFs"
    )

    total_chunks = 0

    for pdf_file in tqdm(pdf_files):

        print(
            f"\nProcessing "
            f"{pdf_file.name}"
        )

        pages = parser.parse_pdf(
            str(pdf_file)
        )

        chunks = chunker.create_chunks(
            pages
        )

        total_chunks += len(chunks)

        process_chunks(
            chunks,
            embedder,
            qdrant
        )

        print(
            f"Inserted "
            f"{len(chunks)} chunks"
        )

    print(
        "\nDone."
    )

    print(
        f"Total chunks: "
        f"{total_chunks}"
    )

    print(
        f"Stored vectors: "
        f"{qdrant.count()}"
    )


if __name__ == "__main__":
    main()