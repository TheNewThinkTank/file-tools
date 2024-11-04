import tempfile
from pathlib import Path
from file_convertion_tools.json_to_yaml import json_to_yaml  # type: ignore


def test_json_to_yaml():
    # Use a temporary directory to avoid file permission issues
    with tempfile.TemporaryDirectory() as tmpdir:
        in_file = Path(tmpdir) / "db.json"
        out_file = Path(tmpdir) / "db.yml"

        # Write JSON content to the input file
        in_file.write_text('{"key": "value"}')

        # Convert JSON to YAML
        json_to_yaml(in_file)

        # Assert the output file was created
        assert out_file.exists()

        # Check the content of the output file
        content = out_file.read_text()
        assert "key: value" in content  # Adjust based on expected YAML output format
