import uuid

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from config import settings


class Chunker:

    def __init__(self):

        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=
                settings.CHUNK_SIZE,

                chunk_overlap=
                settings.CHUNK_OVERLAP,

                separators=[
                    "\n\n",
                    "\n",
                    ". ",
                    " "
                ]
            )
        )

    def create_chunks(
        self,
        parsed_pages
    ):

        chunks = []

        for page in parsed_pages:

            page_chunks = (
                self.splitter.split_text(
                    page["text"]
                )
            )

            for idx, chunk_text in enumerate(
                page_chunks
            ):

                chunks.append(
                    {
                        "chunk_id":
                            str(uuid.uuid4()),

                        "pdf_name":
                            page["pdf_name"],

                        "page_number":
                            page["page_number"],

                        "chunk_index":
                            idx,

                        "text":
                            chunk_text
                    }
                )

        return chunks