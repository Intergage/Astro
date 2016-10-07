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
import click

INTRO = '''
Welcome to the Exo-planet Archive API search
  http://exoplanetarchive.ipac.caltech.edu
'''

@click.group()
def click_grp():
    print(click_grp.command)


def main():
    MENU = '''
    1. Pre-defined search queries
    2. QWizard
    3. Advanced query
    '''

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
            elif menuChoice == '3':
                print('')
                modules.writeAdv()
            elif menuChoice == 'q'.lower():
                print('Bye')
                break

        except IndexError:
            print('Unknown Option %s' % menuChoice)

@click_grp.command()
def write_own():
    #print('DEBUG: write_own')
    modules.writeAdv()

@click_grp.command()
def qwizard():
    #print('DEBUG: qwizard')
    modules.writeOwn()

@click_grp.command()
def pre_defined():
    #print('DEBUG: pre_defined')
    modules.preDefined()



click_grp()