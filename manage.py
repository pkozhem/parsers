"""
    CLI for this application. Type "--help" argument to see usage.
"""

import os
import sys
import argparse


def add_args():
    parser = argparse.ArgumentParser(description='Site parser application.')
    parser.add_argument("health_diet", help="Calling parser for health-diet.ru.")
    parser.add_argument("memorial_royal", help="Calling parser for memorialroyal.by")
    parser.add_argument("zaka_zaka", help="Calling parser for zaka-zaka.com.")
    args = parser.parse_args()
    return args


def call_parser():
    if sys.argv[1] == "health_diet":
        os.system("python3 health_diet_ru_parser/parser.py")

    elif sys.argv[1] == "memorial_royal":
        os.system("python3 memorial_royal_by_parser/parser.py")

    elif sys.argv[1] == "zaka_zaka":
        os.system("python3 zaka_zaka_com_parser/parser.py")

    else:
        print(add_args().help)


def execute_from_command_line():
    if len(sys.argv) > 1:
        call_parser()

    else:
        print(add_args().help)


if __name__ == '__main__':
    execute_from_command_line()
