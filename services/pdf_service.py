from PyPDF2 import PdfReader
import os


def extract_text(file_path: str):

    extension = os.path.splitext(
        file_path
    )[1].lower()

    if extension == ".pdf":

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text

    elif extension == ".txt":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    return None


if __name__=="__main__":

    pdf_file_path = r"test\files_for_test\Kondapalli_CV_2026.pdf"

    text_file_path = r"test\files_for_test\job_description.txt"
    print(extract_text(pdf_file_path))
    