#!env python3
from sys import argv
from pathlib import Path
from docopt import docopt
from icecream import ic
import random

# ic.disable()
ic.configureOutput(includeContext=True, contextAbsPath=False)


doc = f"""Usage:
  ${argv[0]}  [--count=<n>] [--words=<w>] [--dictionary=<d>] [--puzzle=<puzzle>] [--answer=<answer>] [--seed=<seed>] [--verbose=<v>]

Options:
  -h --help           Show this help message.
  --count=<n>         Number of jumbles [default: 1].
  --words=<w>         Words in each of those jumbles [default: 1].
  --dictionary=<d>          Dictionaryionary file [default: words.txt].
  --puzzle=<puzzle>   Puzzle ouput file [default: puzzle.txt].
  --answer=<answer>   Answer ouput file [default: answer.txt].
  --seed=<seed>       Seed for random number generator [default: 0].
  --verbose=<v>       Verbose output [default: False].
"""


def main(count: int, words_pre: int, dictionary_fn: str, out: str, answer_fn: str, seed: int, verbose: bool):
    # ic(count, words_per, dictionary_fn, out,       answer_fn, seed, verbose, type(verbose))
    words = Path(dictionary).read_text().splitlines()
    answers: list[str] = []
    jumbles: list[str] = []
    underbars: str = '-' * (words_per - 1)

    # as a hint we could put the lengths of the words

    random.seed(seed)
    for _ in range(count):
        chosen: lst[str] = random.sample(words, words_pre)
        answers.append(' '.join(chosen))
        jumbles.append(underbars+jumblify(chosen))
    # ic(answers, jumbles)

    Path(answer_fn).write_text("\n".join(answers))
    Path(out).write_text("\n".join(jumbles))


def jumblify(words: list[str]) -> str:
    # ic(words)
    return permutation("".join(words))


def permutation(s: str) -> str:
    strung = list(s)
    random.shuffle(strung)
    return "".join(strung)


if __name__ == "__main__":
    args = docopt(doc)
    count = int(args['--count'])
    words_per = int(args['--words'])
    dictionary = args['--dictionary']
    out = args['--puzzle']
    answer = args['--answer']
    seed = int(args['--seed'])
    verbose = args['--verbose'].lower() == 'true'

    # ic(count, words_per, dictionary, out, answer, seed, verbose, type(verbose))
    main(count, words_per, dictionary, out, answer, seed, verbose)
