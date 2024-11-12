
from itertools import zip_longest


def concatenate_files(file1: str, file2: str, outfile: str='out.txt') -> None:
    with open(file1) as f1, open(file2) as f2, open(outfile, 'w') as wf:
        for left, right in zip_longest(f1, f2, fillvalue=''):
            wf.write(left.rstrip('\n') + right)
