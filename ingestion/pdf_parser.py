import fitz
from pathlib import Path

from ingestion.ocr import OCRProcessor
import re

def clean_text(text):

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


class PDFParser:

    def __init__(self):

        self.ocr = OCRProcessor()

    def parse_pdf(
        self,
        pdf_path: str
    ):

        doc = fitz.open(pdf_path)

        pages = []

        for page_num in range(len(doc)):

            page = doc[page_num]

            text = page.get_text()

            # fallback OCR
            if len(text.strip()) < 50:

                pix = page.get_pixmap(
                    matrix=fitz.Matrix(2, 2)
                )

                image_bytes = pix.tobytes("png")

                text = self.ocr.extract_text_from_image_bytes(
                    image_bytes
                )

            pages.append(
                {
                    "pdf_name":
                        Path(pdf_path).name,

                    "page_number":
                        page_num + 1,

                    "text":
                        text
                }
            )

        doc.close()

        return pages