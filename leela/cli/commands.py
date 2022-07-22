# https://www.youtube.com/watch?v=pXhcPJK5cMc&t=1294s&ab_channel=VladimirKeleshev
#!/usr/bin/env python
# usage: [--version] [--help] command [<args>...]
"""
Leela Command Line Interface

Usage:
    leela run_test <test_number>
    leela run_all_tests
    leela start_db
    leela stop_db
    leela build_db [options]
    leela delete_db
    leela query_db
    leela load_freddie
    leela load_fannie
    leela load_fannie_sample
    leela download_freddie_mac
    leela download_fannie_mae
    leela update_database
    leela backtest

Options:
    --full
"""


import os
from docopt import docopt

from leela.cli.commands.start_db import start_db
from leela.cli.commands.stop_db import stop_db
from leela.cli.commands.load_freddie_to_db import load_freddie_to_db
from leela.cli.commands.load_freddie_to_db import load_freddie_to_db
from leela.cli.commands.load_fannie import load_fannie
from leela.cli.commands.download_freddie_mac import download_freddie_mac
from leela.cli.commands.download_fannie_mae import download_fannie_mae
from leela.cli.commands.build_db import build_db
from leela.cli.commands.delete_db import delete_db
from leela.cli.commands.run_all_tests import run_all_tests
from leela.cli.commands.run_test import run_test
from leela.cli.commands.query_db import query_db

from leela.config import config

# --------------------------------------------------------------------- #
#   TODO:
# --------------------------------------------------------------------- #
#   1. Load Fannie/Freddie Data
#   2. Foo()
# --------------------------------------------------------------------- #

def main():
    
    args = docopt(__doc__, help=True)
    
    if args['run_test']:
        run_test()
    elif args['run_all_tests']:
        run_all_tests()
    elif args['start_db']:
        start_db()
    elif args['stop_db']:
        stop_db()
    elif args['build_db']:
        build_db()
    elif args['delete_db']:
        delete_db()
    elif args['query_db']:
        query_db()
    elif args['load_fannie']:
        # load_fannie(start=5, limit=10)
        load_fannie(start=None, limit=20)
    elif args['load_fannie_sample']:
        # load_fannie(limit=2)
        load_fannie(limit=3)
    elif args['download_fannie_mae']:
        # download_fannie_mae("2021", "Q4")
        download_fannie_mae("2021", "Q4")
    elif args['download_freddie_mac']:
        download_freddie_mac()
    elif args['load_freddie_to_db']:
        load_freddie_to_db()


if __name__ == "__main__":
    # References ->
    # https://www.johnhcochrane.com/
    # https://capitalmarkets.fanniemae.com/credit-risk-transfer/single-family-credit-risk-transfer/fannie-mae-single-family-loan-performance-data
    DEBUG = False
    
    # Set Postgres SQL options ->

    os.environ["PGDATA"] = config.POSTGRES_DIR

    if DEBUG:
        print("DEBUG TEST")
    else:
        main()