
from pypdf import PdfReader


def pdf_to_txt(pdf_file: str) -> None:

    reader = PdfReader(pdf_file)
    txt_file = pdf_file.removesuffix("pdf") + "txt"
    content = [
        f"{reader.metadata.title}",
        f"Number of pages: {len(reader.pages)}"
    ]
    for page in reader.pages:
        content.append(page.extract_text())
    txt_file.write_text("\n".join(content))
