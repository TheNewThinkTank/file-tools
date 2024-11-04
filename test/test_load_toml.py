
from unittest.mock import mock_open, patch
from file_convertion_tools.load_toml import load_toml


def test_load_toml():

    toml_content = b"""
    [section]
    key = "value"
    """

    expected_result = {"section": {"key": "value"}}

    # Mock open and tomllib.load
    with patch("builtins.open", mock_open(read_data=toml_content)) as mock_file:
        with patch("tomllib.load", return_value=expected_result) as mock_toml_load:
            # Call the function with a dummy file path
            result = load_toml("dummy.toml")

            # Check if open was called with the correct file path and mode
            mock_file.assert_called_once_with("dummy.toml", "rb")
            # Check if tomllib.load was called correctly
            mock_toml_load.assert_called_once()

            # Assert that the result is as expected
            assert result == expected_result
