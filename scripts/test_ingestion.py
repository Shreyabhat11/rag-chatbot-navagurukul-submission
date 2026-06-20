from ingestion.pdf_parser import PDFParser
from ingestion.chunker import Chunker

parser = PDFParser()

pages = parser.parse_pdf(
    "data/pdfs/00-0 Head_First_Java_Second_Edition.pdf"
)

print(
    f"Pages Extracted: {len(pages)}"
)

chunker = Chunker()

chunks = chunker.create_chunks(
    pages
)

print(
    f"Chunks Generated: {len(chunks)}"
)

print("\nSample Chunk:\n")
print(chunks[0]["text"][:1000])