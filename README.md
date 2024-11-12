
<a href="https://pypi.org/project/file-convertion-tools/">
<img src="https://img.shields.io/pypi/v/file-convertion-tools.svg">
</a>
<a href="https://github.com/TheNewThinkTank/msgspec/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/TheNewThinkTank/file-tools.svg">
</a>

![PyPI Downloads](https://img.shields.io/pypi/dm/file-convertion-tools)
![CI](https://github.com/TheNewThinkTank/file-tools/actions/workflows/wf.yml/badge.svg)
[![codecov](https://codecov.io/gh/TheNewThinkTank/file-tools/graph/badge.svg?token=hCgj5V8QwP)](https://codecov.io/gh/TheNewThinkTank/file-tools)
![commit activity](https://img.shields.io/github/commit-activity/m/TheNewThinkTank/file-tools)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/file-tools?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/file-tools/archive/refs/heads/main.zip)

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
