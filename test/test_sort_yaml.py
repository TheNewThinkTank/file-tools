
import os
import yaml
import pytest
from tempfile import NamedTemporaryFile
from file_convertion_tools.sort_yaml import sort_yaml


@pytest.fixture
def unsorted_yaml_content():
    return {
        "banana": "yellow",
        "apple": "red",
        "grape": "purple",
        "cherry": "red",
    }


@pytest.fixture
def sorted_yaml_content():
    return {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red",
        "grape": "purple",
    }


def test_sort_yaml(unsorted_yaml_content, sorted_yaml_content):
    # Create a temporary file for the unsorted YAML content
    with NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
        yaml.dump(unsorted_yaml_content, tmp_file)
        tmp_file_path = tmp_file.name

    # Call the sort_yaml function to sort the content
    sort_yaml(tmp_file_path)

    # Verify the file content is sorted
    with open(tmp_file_path, 'r') as tmp_file:
        result = yaml.safe_load(tmp_file)

    # Check if the result matches the expected sorted content
    assert result == sorted_yaml_content

    # Clean up the temporary file
    os.remove(tmp_file_path)
