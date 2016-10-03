# Testing Git Push

'''
API:                        http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data
Pre-generate API Queries:   http://exoplanetarchive.ipac.caltech.edu/docs/API_queries.html
Format control:             &format=JSON
Get Columns for table:      table=exoplanets&getDefaultColumns


Example:
    <Standard URL>nph-nstedAPI?table=<TABLENAME>&select=<COLUMN NAMES,CAN HAVE MANY>


############# EXAMPLE CODE #############
query = ("http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&where=*&format=JSON")
raw_data = pd.read_json(query)

print(raw_data)
########################################

'''

import numpy as np
import pandas as pd
import datetime
import urllib
import sys
import argparse
import modules

'''
parser = argparse.ArgumentParser(description='Astro API Search')
parser.add_argument('--pre-defined', help='Pre-defined search queries')
parser.add_argument('--write-own', help='Write your own query')

args = parser.parse_args()
'''

table_lists = [('Confirmed Planets', ['exoplanets', 'multiexopars']), ('KOI (Cumulative)', ['cumulative', 'q1_q17_dr24_koi', 'q1_q16_koi', 'q1_q12_koi', 'q1_q8_koi', 'q1_q6_koi']),
               ('Threshold-Crossing Events (TCEs)', ['q1_q17_dr25_tce', 'q1_q17_dr24_tce', 'q1_q16_tce', 'q1_q12_tce'])]


print('''
Welcome to the Exo-planet Archive API search
  http://exoplanetarchive.ipac.caltech.edu
''')
def main():
    MENU = '''
    1. Pre-defined search queries
    2. Write your own query
    3. Advanced query
    '''

    KEYS = {'1': 'Pre Defined search query',
            '2': 'Write your own query',
            '3': 'Advanced query',
            'q': 'Quit'}

    while True:
        print(MENU)
        try:
            menuChoice = input('_> ')
            if menuChoice == '1':
                print('')
                modules.preDefined()
            elif menuChoice == '2':
                print('''
                     Build your own query
----------------------------------------------------------------------------
           For all table, column and data names please see
http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data

        I have tried to make it as easy as I can to create
        your own query without learning the correct syntax

        Tables are split into categories for ease of use.
        Please select what category you'd like to explore.\n\n
                ''')
                temp = []
                for x, y in table_lists:
                    temp.append(x)

                for i, name in enumerate(temp):
                    print(i, '-', "{0:20}".format(name), end='\n' if i%10==4 else ' ')
                print('\n')

                category = input('Category? _> ')
                print('\n')

                print('*'*40, 'TABLE NAMES', '*'*40, '\n')
                for i, name in enumerate(table_lists[int(category)][1]):
                    print("{0:20}".format(name), end='\n' if i%10==4 else ' ')
                print('\n')
                print('*'*93, '\n')

                table = input('Table? _> ')

                print('Gathering table columns')
                modules.getColumns(table)

                print('''
        These are the columns for the selected table
        You need to select what columns to return
        You can select a single column or multiple
        Separate them with a comma(,)
                ''')

                column = input('Column(s)? _> ')

                print('''
        Now we can set arguments for our query.
        You will need to know basic SQL (SoQL(?))
            http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#syntax
                ''')

                # TODO Find some way only add 'select', 'where', etc unless the user really wants to. EG: table=cumulative&select=kepid&where=* wont work but table=cumulative&select=kepid will.
                choice = input('Write Arguments? y/n_> ')
                if choice.lower() == 'y':
                    argz = input('Arguments _> ')
                    url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=' + table + '&select=' + column + '&where=' + argz + '&format=JSON'
                    data = modules.querySend(url)
                    print(data)
                elif choice.lower() == 'n':
                    print('Returning all data from selected columns')
                    url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=' + table + '&select=' + column + '&format=JSON'
                    data = modules.querySend(url)
                    print('Query Used: ' + url + '\n')
                    print(data)
                else:
                    print('Input not valid')


            elif menuChoice == 'q'.lower():
                print('Bye')
                break

        except IndexError:
            print('Unknown Option %s' % menuChoice)


if __name__ == '__main__':
    try:
        if sys.argv[1] == '--pre-defined':
            modules.preDefined()
        elif sys.argv[1] == '--write-own':
            print('DO THIS - Modulate Write own?')
        else:
            print('Unknown Arg')
    except:
        main()
