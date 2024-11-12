
import tempfile
import os

from file_convertion_tools.count_pdf_pages import count_pages


def create_test_pdf(num_pages):
    """Helper function to create a simple PDF file
    with a specific number of /Type /Page entries."""
    pdf_content = b"%PDF-1.4\n"
    for _ in range(num_pages):
        pdf_content += b"1 0 obj\n<< /Type /Page >>\nendobj\n"
    pdf_content += b"%%EOF\n"
    return pdf_content


def test_count_pages_single_page():
    # Test a PDF file with a single page
    pdf_content = create_test_pdf(1)
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(pdf_content)
        temp_pdf_name = temp_pdf.name
    
    try:
        assert count_pages(temp_pdf_name) == 1
    finally:
        os.remove(temp_pdf_name)


def test_count_pages_multiple_pages():
    # Test a PDF file with multiple pages
    pdf_content = create_test_pdf(5)
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(pdf_content)
        temp_pdf_name = temp_pdf.name

    try:
        assert count_pages(temp_pdf_name) == 5
    finally:
        os.remove(temp_pdf_name)


def test_count_pages_no_pages():
    # Test a PDF file with no pages
    pdf_content = b"%PDF-1.4\n%%EOF\n"
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(pdf_content)
        temp_pdf_name = temp_pdf.name

    try:
        assert count_pages(temp_pdf_name) == 0
    finally:
        os.remove(temp_pdf_name)


def test_count_pages_non_pdf_file():
    # Test with a non-PDF file (should return 0)
    non_pdf_content = b"This is just some random text and not a PDF file."
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(non_pdf_content)
        temp_pdf_name = temp_pdf.name

    try:
        assert count_pages(temp_pdf_name) == 0
    finally:
        os.remove(temp_pdf_name)
