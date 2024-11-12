
import re

rxcountpages = re.compile(
    r"/Type\s*/Page(?=[\s/])",
    re.MULTILINE | re.DOTALL
)


def count_pages(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return len(rxcountpages.findall(data.decode('latin1')))


if __name__ == "__main__":
    print("Number of pages in PDF File:", count_pages("test.pdf"))
