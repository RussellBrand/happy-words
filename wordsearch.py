# wordsearch.py
#!env python3
import sys
from sys import argv
# from pathlib import Path
# from docopt import docopt  # type: ignore
from icecream import ic
import random
from typing import Final
from termcolor import colored


# ic.disable()
ic.configureOutput(includeContext=True, contextAbsPath=False)

# make this a variable
CAPTIALIZE: Final[bool] = True

doc = f"""Usage:
  ${argv[0]}  [--x=<x>] [--words=<w>] [--y=<y>] [--retries=<r>] [--verbose=<v>] [--dictionary=<d>] [--puzzle=<puzzle>] [--answer=<answer>] [--seed=<seed>]

Options:
  -h --help           Show this help message.
  --x=<x>             Columns in the puzzle [default: 60].
  --y=<y>               Rows in the puzzle [default: 10].
  --words=<w>         Number of words to hide [default: 1].
  --dictionary=<d>          Dictionaryionary file [default: words.txt].
  --puzzle=<puzzle>   Puzzle ouput file [default: puzzle.txt].
  --answer=<answer>   Answer ouput file [default: answer.txt].
  --seed=<seed>       Seed for random number generator [default: 0].
  --verbose=<v>       Verbose output [default: False].
"""


FILLER: Final[str] = '.'


def main(count: int, dictionary_fn: str, out: str, answer_fn: str, search_list: str, seed: int, verbose: bool, x: int, y: int) -> None:
    random.seed(seed)
    # use pathlib
    with open(dictionary_fn) as f:
      # could control direction rather than just stripping out long words.
        words = [line.strip() for line in f if len(line.strip()) < min(x, y)]
    puzzle: list[list[str]] = [[FILLER for _ in range(x)] for _ in range(y)]
    # for when I do diangles
    # directions: list[tuple[int, int]] = [(0,0),(0,1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
    # ic(puzzle)

    chosen_words = random.sample(words, count)
    skipped_words: set[str] = set()
    # why can't i import and use type Color ??
    directions_list: list[tuple[int, int, str]] = [(1, 0, "red"), (0, 1, "green"),
                                                   (1, 1, "blue"), (-1, 0, "yellow"), (0, -1, "magenta"), (-1, -1, "cyan"), (1, -1, "white"), (-1, 1, "grey")]
    for wd in chosen_words:
        wd: str
        placed = False
        # attempts should be a variable
        attempts = 5
        # the stuff in this while loop should be factored out for unit testing

        while not placed and attempts > 0:
            dx, dy, color = random.choice(directions_list)
            dx: int
            dy: int

            # ic(dx, dy, wd)

            if dx == 0:
                sx = random.randrange(x)
            elif dx > 0:
                sx = random.randrange(x - len(wd) + 1)
            else:
                sx = random.randrange(len(wd) - 1, x)

            if dy == 0:
                sy = random.randrange(y)
            elif dy > 0:
                sy = random.randrange(y - len(wd) + 1)
            else:
                sy = random.randrange(len(wd) - 1, y)

            if all(puzzle[sy + i*dy][sx + i*dx] == FILLER for i in range(len(wd))):
                if CAPTIALIZE:
                    wd = wd.capitalize()
                for i, letter in enumerate(wd):
                    # type: ignore
                    # type: ignore
                    puzzle[sy + i*dy][sx + i*dx] = colored(letter, color)
                    # letter

                placed = True
            attempts -= 1
        if not placed:
            print(f"Warning: could not place {wd}", file=sys.stderr)
            skipped_words.add(wd)

    print('\nPuzzle:\n')
    print(puzzle_to_str(puzzle))
    # exit(0)
    with open(answer_fn, 'w') as f:
        for word in words:
            f.write(word + '\n')
    print(f'Answer written to {answer_fn}')

    obscured_puzzle: list[list[str]] = puzzle_obscurify(puzzle)
    print('\nObscured puzzle:\n')
    print(puzzle_to_str(obscured_puzzle))
    with open(out, 'w') as f:
        for row in puzzle:
            f.write(''.join(row) + '\n')

    print(f'Puzzle written to {out}')

    with open(search_list, 'w') as f:
        for word in chosen_words:
            if word not in skipped_words:
                f.write(word + '\n')

    print(f'Search list written to {search_list}')


def puzzle_obscurify(puzzle: list[list[str]]) -> list[list[str]]:
    answer: list[list[str]] = []
    for line in puzzle:
        answer.append([random_letter() if c == FILLER else c for c in line])
    return answer


def random_letter() -> str:
    return chr(random.randint(ord('a'), ord('z')))


def puzzle_to_str(puzzle: list[list[str]]) -> str:
    return '\n'.join(''.join(row) for row in puzzle)


if __name__ == '__main__':
    main(5,   'words.txt', 'puzzle.txt', 'answer.txt',
         'search-list.txt', 0, False, 60, 10)

    # args = docopt(doc)
    # ic(args)
    # main(int(args['--words']), args['--dictionary'], args['--puzzle'], args['--answer'], int(args['--seed']), args['--verbose'], int(args['--x']), int(args['--y']))
