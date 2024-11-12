
import pytest
from unittest.mock import patch, MagicMock
from file_convertion_tools.pdf_to_csv_tabula import get_area, inspect_first_table, show_tables, convert_pdf_to_csv, convert_batch

# Mock PDF file name for testing
TEST_PDF_FILE = "test_document.pdf"


@pytest.fixture
def mock_table_data():
    """
    Fixture to provide mock table data.
    """
    return [{
        "top": 50,
        "left": 30,
        "height": 200,
        "width": 300,
    }]


@patch("file_convertion_tools.pdf_to_csv_tabula.read_pdf")
def test_get_area(mock_read_pdf, mock_table_data):
    """
    Test get_area function to ensure it calculates area correctly.
    """
    mock_read_pdf.return_value = mock_table_data
    area = get_area(TEST_PDF_FILE)
    assert area == [30, 10, 260, 340]



@patch("file_convertion_tools.pdf_to_csv_tabula.read_pdf")
def test_inspect_first_table(mock_read_pdf):
    """
    Test inspect_first_table to ensure correct processing and print output.
    """
    # Mock DataFrame returned from read_pdf
    mock_df = MagicMock()
    mock_df.head.return_value = mock_df
    mock_read_pdf.return_value = [mock_df]

    # Run and check the function's behavior
    inspect_first_table(TEST_PDF_FILE)
    # mock_read_pdf.assert_called_once_with(TEST_PDF_FILE, multiple_tables=True, pages=1, area=[30, 10, 260, 330], silent=True)
    mock_df.head.assert_called_once_with(7)


# @patch("file_convertion_tools.pdf_to_csv_tabula.read_pdf")
# def test_show_tables(mock_read_pdf, mock_table_data):
#     """
#     Test show_tables to ensure all tables are displayed correctly.
#     """
#     mock_df1, mock_df2 = MagicMock(), MagicMock()
#     mock_read_pdf.return_value = [mock_df1, mock_df2]

#     # Run the function and validate calls
#     show_tables(TEST_PDF_FILE)
#     assert mock_read_pdf.call_count == 1
#     assert len(mock_read_pdf.return_value) == 2


# @patch("file_convertion_tools.pdf_to_csv_tabula.convert_into")
# @patch("file_convertion_tools.pdf_to_csv_tabula.get_area", return_value=[30, 10, 260, 330])
# def test_convert_pdf_to_csv(mock_convert_into):
#     """
#     Test convert_pdf_to_csv to ensure it converts and saves CSV correctly.
#     """
#     convert_pdf_to_csv(TEST_PDF_FILE)
#     output_file = TEST_PDF_FILE.replace(".pdf", ".csv")
#     mock_convert_into.assert_called_once_with(TEST_PDF_FILE, output_file, output_format="csv", pages="all", area=[30, 10, 260, 330], silent=True)


@patch("file_convertion_tools.pdf_to_csv_tabula.convert_into_by_batch")
def test_convert_batch(mock_convert_into_by_batch):
    """
    Test convert_batch to ensure it processes all PDFs in a directory.
    """
    directory = "./pdf_files"
    convert_batch(directory)
    mock_convert_into_by_batch.assert_called_once_with(directory, output_format="csv", pages="all", silent=True)
