# encoding: utf8
# Sunday's Iron

from termcolor import cprint
from click import command, option


@command()
@option()
def pack():
    pass


if __name__ == '__main__':
    cprint("Sunday's Iron command line texture packing tool", 'yellow')
