
import yaml


def sort_yaml(file_path: str, output_path: str = None) -> None:
    """_summary_

    :param file_path: _description_
    :type file_path: str
    :param output_path: _description_, defaults to None
    :type output_path: str, optional
    :raises ValueError: _description_
    """

    # Load the YAML content
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Check if data is a dictionary, as sorting only applies to mappings
    if isinstance(data, dict):
        # Sort the dictionary by key
        sorted_data = dict(sorted(data.items()))
    else:
        raise ValueError("The YAML file does not contain a dictionary structure")

    # Determine the output path (overwrite if output_path is not provided)
    output_path = output_path or file_path

    # Write the sorted content back to YAML format
    with open(output_path, 'w') as file:
        yaml.dump(sorted_data, file, sort_keys=False)

    print(f"YAML content sorted and saved to {output_path}")
