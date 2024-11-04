
import tomllib


def load_toml(toml_file: str) -> dict:
    """_summary_

    :param toml_file: _description_
    :type toml_file: str
    :return: _description_
    :rtype: dict
    """

    with open(toml_file, 'rb') as rf:
        toml_data: dict = tomllib.load(rf)
        return toml_data
