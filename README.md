# file-tools

common file conversions

## Installation

```BASH
pip install file-convertion-tools
```

## Usage example

Importing example

```Python
from file_convertion_tools.load_toml import load_toml
```

Usage

```Python
from pprint import pprint as pp

data: dict = load_toml("some_file.toml")
pp(data, sort_dicts=False)
```

<!--
## Create a new release

example:

```BASH
git tag 0.0.1
git push origin --tags
```

release a patch:

```BASH
poetry version patch
```

then `git commit`, `git push` and

```BASH
git tag 0.0.2
git push origin --tags
```
-->
