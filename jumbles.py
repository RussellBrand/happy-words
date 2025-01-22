from sys import argv 
from docopt import docopt

doc = f"""Usage:
  ${argv[0]}  [--count=<n>]

Options:
  -h --help     Show this help message.
  --count=<n>   Number of times to jumbles [default: 1].
"""

if __name__ == "__main__":
    args = docopt(doc)
    count = int(args['--count'])
    print(f"count = {count}")
