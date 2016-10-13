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

import sys
import modules
from prettytable import PrettyTable

INTRO = '''
Welcome to the Exo-planet Archive API search
  http://exoplanetarchive.ipac.caltech.edu
'''

def main():

    while True:
        MENU = '''
        1. Pre-defined search queries
        2. Advanced Menu
        3. Planet Overview

        q. Quit
        '''

        MENU_d = {
            '1': modules.preDefined,
            '2': menu_2,
            '3': modules.planetOverview,
            'q': exit
        }

        print(MENU)

        func = input('_> ')

        MENU_d.get(func)()

def menu_2():

        MENU = '''
        1. QWizard
        2. Advanced Query Writer (No help)

        b. Main Menu
        '''

        MENU_d = {
            '1': modules.writeOwn,
            '2': modules.writeAdv,
            'b': main,
        }

        print(MENU)

        func = input('_> ')

        MENU_d.get(func)()


print(INTRO)
main()