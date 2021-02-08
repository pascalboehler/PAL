#
# pal.py
# Created 6.02.2021
# by Pascal Boehler
#

import argparse

parser = argparse.ArgumentParser(prog='pal', description='PAL: Personal Automation Assistant')

parser.add_argument('command', metavar='command', type=str, nargs="+",
                    help='test')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()

# go through all possible arguments:

def pal_main():
    print("halloWelt")

'''
if __main__:
    pal_main()

    '''