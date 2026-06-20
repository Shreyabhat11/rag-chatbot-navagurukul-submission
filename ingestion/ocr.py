from PIL import Image
import pytesseract
import io


class OCRProcessor:

    def extract_text_from_image_bytes(
        self,
        image_bytes: bytes
    ) -> str:

        try:

            image = Image.open(
                io.BytesIO(image_bytes)
            )

            text = pytesseract.image_to_string(
                image,
                lang="eng"
            )

            return text.strip()

        except Exception as e:

            print(
                f"OCR Error: {e}"
            )

            return ""