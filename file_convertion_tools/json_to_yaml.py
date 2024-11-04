import json
import yaml  # type: ignore
from pathlib import Path


def json_to_yaml(in_file: Path) -> None:
    """Create YAML file from JSON file, without sorting keys alphabetically.

    :param in_file: absolute path to JSON file
    :type in_file: Path
    """

    output_file = in_file.with_suffix('.yml')

    with open(in_file, 'r') as rf, open(output_file, "w") as wf:
        yaml.dump(json.load(rf), wf, sort_keys=False)
