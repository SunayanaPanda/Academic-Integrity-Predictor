import os
import tempfile
import pdfplumber
from docx import Document


def read_file(file):
    """
    Reads uploaded TXT, PDF, or DOCX files and returns extracted text.
    """

    if not file or file.filename == "":
        return ""

    extension = os.path.splitext(file.filename)[1].lower()

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as temp:
        temp.write(file.read())
        temp_path = temp.name

    extracted_text = ""

    try:
        if extension == ".txt":
            with open(temp_path, "r", encoding="utf-8") as f:
                extracted_text = f.read()

        elif extension == ".pdf":
            with pdfplumber.open(temp_path) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() or ""

        elif extension == ".docx":
            document = Document(temp_path)
            extracted_text = "\n".join(
                paragraph.text for paragraph in document.paragraphs
            )

    except Exception as e:
        print(f"Error reading {file.filename}: {e}")
        return ""

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return extracted_text.strip()


def allowed_file(filename):
    """
    Checks whether the uploaded file format is supported.
    """

    allowed_extensions = {"txt", "pdf", "docx"}

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )