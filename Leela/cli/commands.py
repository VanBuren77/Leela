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



from leela.cli.commands.download_freddie_mac import download_freddie_mac
from leela.cli.commands.download_fannie_mae import download_fannie_mae
