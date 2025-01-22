A Python library that can generate an argument parser from a usage string is [`argh`](https://argh.readthedocs.io/). This library simplifies argument parsing by using function signatures and docstrings to define the command-line interface. 

### Example with `argh`
```python
import argh

# Define your function with parameters
def greet(name: str, times: int = 1):
    """
    Greets the user.

    :param name: Name of the person to greet.
    :param times: Number of times to repeat the greeting.
    """
    for _ in range(times):
        print(f"Hello, {name}!")

# Create the parser and dispatch the commands
parser = argh.ArghParser()
parser.add_commands([greet])

if __name__ == "__main__":
    parser.dispatch()
```

Running this script will generate a command-line interface:
```bash
$ python script.py greet --name Alice --times 3
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

Another option, if you specifically want a library that can parse a usage string like those seen in `argparse` examples, is the [`docopt`](https://docopt.org/) library. It uses a usage string to define the CLI:

### Example with `docopt`
```python
from docopt import docopt

doc = """Usage:
  my_program.py greet <name> [--times=<n>]

Options:
  -h --help     Show this help message.
  --times=<n>   Number of times to greet [default: 1].
"""

if __name__ == "__main__":
    args = docopt(doc)
    name = args['<name>']
    times = int(args['--times'])
    for _ in range(times):
        print(f"Hello, {name}!")
```

Running this script works similarly:
```bash
$ python script.py greet Alice --times=3
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

Both `argh` and `docopt` are great choices, depending on whether you prefer to define the CLI through function signatures or usage strings.
