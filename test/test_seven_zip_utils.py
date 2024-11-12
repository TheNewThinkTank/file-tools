
import os
import tempfile
import pytest
from file_convertion_tools.seven_zip_utils import (
    extract_7zip_file,
    compress_folder_to_7zip
    )


@pytest.fixture
def temp_dir():
    """Fixture that provides a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


def test_compress_folder_to_7zip(temp_dir):
    # Set up a test folder with sample files
    test_folder = os.path.join(temp_dir, "test_folder")
    os.makedirs(test_folder)
    
    # Create a sample file in the test folder
    sample_file = os.path.join(test_folder, "sample.txt")
    with open(sample_file, "w") as f:
        f.write("Sample content")

    # Define the path for the output .7z file
    output_file = os.path.join(temp_dir, "compressed_test.7z")

    # Run the compression function
    compress_folder_to_7zip(test_folder, output_file)

    # Assert that the .7z file was created
    assert os.path.isfile(output_file)


def test_extract_7zip_file(temp_dir):
    # Set up a test folder and a sample .7z file for extraction
    test_folder = os.path.join(temp_dir, "test_folder")
    os.makedirs(test_folder)
    
    # Create a sample file in the test folder
    sample_file = os.path.join(test_folder, "sample.txt")
    with open(sample_file, "w") as f:
        f.write("Sample content")

    # Define the path for the .7z archive
    archive_file = os.path.join(temp_dir, "compressed_test.7z")
    compress_folder_to_7zip(test_folder, archive_file)

    # Create a new directory to extract files into
    extraction_folder = os.path.join(temp_dir, "extracted_folder")
    os.makedirs(extraction_folder)

    # Run the extraction function
    extract_7zip_file(archive_file, extraction_folder)

    # Assert that the file was extracted correctly
    extracted_file = os.path.join(
        extraction_folder,
        "test_folder",
        "sample.txt"
        )
    assert os.path.isfile(extracted_file)

    # Verify content
    with open(extracted_file, "r") as f:
        content = f.read()
    assert content == "Sample content"


def test_extract_nonexistent_file():
    # Test extracting a non-existent .7z file
    with pytest.raises(FileNotFoundError):
        extract_7zip_file("non_existent_file.7z")


def test_compress_nonexistent_folder():
    # Test compressing a non-existent folder
    with pytest.raises(NotADirectoryError):
        compress_folder_to_7zip("non_existent_folder", "output.7z")
