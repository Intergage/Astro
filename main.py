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
import argparse
'''
parser = argparse.ArgumentParser(description='Astro API Search')
parser.add_argument('--pre-defined', help='Pre-defined search queries')
parser.add_argument('--write-own', help='Write your own query')
args = parser.parse_args()
'''

intro = '''
Welcome to the Exo-planet Archive API search
  http://exoplanetarchive.ipac.caltech.edu
'''

arg_help = [('Pre-defined Queries: ', ['[--pre-defined]', 'A list of queries taken from http://exoplanetarchive.ipac.caltech.edu/docs/API_queries.html']),
            ('Build your own query: ', ['[--write-own]', 'Use a \'wizard\' style module to help create queries']),
            ('Write advanced query: ', ['[--write-adv]', 'A prompt that will allow you to write your own query from scratch. MUST KNOW API SYNTAX'])]

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
                print('')
                modules.writeOwn()
            elif menuChoice == 'q'.lower():
                print('Bye')
                break

        except IndexError:
            print('Unknown Option %s' % menuChoice)

if __name__ == '__main__':
    try:
        if sys.argv[1] == '--pre-defined':
            print(intro)
            modules.preDefined()
        elif sys.argv[1].lower() == '-h' or sys.argv[1].lower() == '-help':
            for arg_name, arg_options in arg_help:
                print('\t', arg_name, arg_options[0], '\n\t\t', arg_options[1], '\n')
        elif sys.argv[1] == '--write-own':
            print(intro)
            modules.writeOwn()
        elif sys.argv[1] == '--write-adv':
            print(intro)
            modules.writeAdv()
        else:
            print('Unknown Arg')
    except:
        main()
