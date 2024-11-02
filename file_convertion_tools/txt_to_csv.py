"""_summary_
"""

import pandas as pd  # type: ignore


def txt_to_csv(in_file: str, sep: str = ",") -> None:
    """Create csv file from txt using Pandas.

    :param in_file: name of txt file
    :type in_file: str
    :param sep: _description_, defaults to ','
    :type sep: str, optional
    """

    df = pd.read_csv(in_file, sep=sep)

    df.to_csv(in_file.split(".")[0] + ".csv", index=False)
