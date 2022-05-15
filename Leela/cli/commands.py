# https://www.youtube.com/watch?v=pXhcPJK5cMc&t=1294s&ab_channel=VladimirKeleshev
#!/usr/bin/env python
# usage: [--version] [--help] command [<args>...]
"""
Leela Command Line Interface

Usage:
    leela run_test <test_number>
    leela run_all_tests
    leela build_db [options]
    leela delete_db
    leela update_database
    leela query_db
    leela backtest

Options:
    --full
"""

from docopt import docopt

from leela.cli.commands.load_freddie_to_db import load_freddie_to_db
from leela.cli.commands.load_fannie_to_db import load_fannie_to_db
from leela.cli.commands.download_freddie_mac import download_freddie_mac
from leela.cli.commands.download_fannie_mae import download_fannie_mae
from leela.cli.commands.build_db import build_db
from leela.cli.commands.delete_db import delete_db
from leela.cli.commands.run_all_tests import run_all_tests
from leela.cli.commands.run_test import run_test
from leela.cli.commands.query_db import query_db

# -------------------------------------------------------------------------------- #
#   #TODO:
# -------------------------------------------------------------------------------- #
#   1. Load Fannie/Freddie Data
#   2. 
# -------------------------------------------------------------------------------- #

def main():
    
    args = docopt(__doc__, help=True)
    
    if args['run_test']:
        run_test()
    elif args['run_all_tests']:
        run_all_tests()
    elif args['build_db']:
        build_db()
    elif args['delete_db']:
        delete_db()
    elif args['query_db']:
        query_db()
    elif args['load_fannie_to_db']:
        load_fannie_to_db()
    elif args['load_freddie_to_db']:
        load_freddie_to_db()
    elif args['download_fannie_mae']:
        download_fannie_mae()
    elif args['download_freddie_mac']:
        download_fannie_mae()


if __name__ == "__main__":

    DEBUG = False
    
    if DEBUG:
        print("DEBUG TEST")
    else:
        main()