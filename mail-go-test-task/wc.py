import sys

args = sys.argv
if len(args) < 2:
    raise RuntimeError('You did not Enter filepath. Right usage is python3 wc.py [filepath]')
filename = args[-1]

with open(filename, 'r') as fp:
    num_lines = sum(1 for line in fp)
print(num_lines)


