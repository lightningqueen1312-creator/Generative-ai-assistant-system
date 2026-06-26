import PyPDF2


def read_pdf(pdf_file):
    """
    Reads a PDF file and returns all text.
    """

    text = ""

    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text