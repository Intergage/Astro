import pandas as pd
from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs
import re

table_lists = [('Confirmed Planets', ['exoplanets', 'multiexopars']),
               ('KOI (Cumulative)', ['cumulative', 'q1_q17_dr24_koi', 'q1_q16_koi', 'q1_q12_koi', 'q1_q8_koi', 'q1_q6_koi']),
               ('Threshold-Crossing Events', ['q1_q17_dr25_tce', 'q1_q17_dr24_tce', 'q1_q16_tce', 'q1_q12_tce']),
               ('K-Stellar Properties', ['keplerstellar', 'q1_q17_dr25_stellar', 'q1_q17_dr24_stellar', 'q1_q16_stellar', 'q1_q12_stellar', 'keplertimeseries', 'keplernames']),
               ('KELT Time Series', ['kelttimeseries', 'EG: &kelt_field=N02']),
               ('SuperWASP Time Series', ['superwasptimeseries', 'EG: &tile=tile168060  OR  &sourceid=1SWASP J191645.46+474912.3']),
               ('K2', ['k2targets', 'k2candidates', 'k2names']),
               ('Mission Stars', ['missionstars', 'mission_exocat'])]


def preDefined():
    print('Pre-defined search queries from caltech.edu\n')
    while True:
        MENU = {1: 'All confirmed planets and columns',
                2: 'Confirmed planets in the Kepler field (default columns)',
                3: 'Stars known to host exoplanets listed in ascending order',
                4: 'Confirmed planets that transit their host stars (default columns)',
                5: 'A current list of non-confirmed planet candidates',
                6: 'K2 targets from campaign 9',
                7: 'Confirmed planets in the Mission Star list',
                8: 'All default parameters for one particular KOI or another',
                9: 'All microlensing planets with time series',
                10: 'All planetary candidates smaller than 2Re with equilibrium temperatures between 180-303K'}

        options = sorted(MENU.keys())
        for opt in options:
            print(opt, '\t', MENU[opt])
        print('\n')

        choice = input('_> ')
        print('\n')

        try:
            if choice == '1':
                print('Query Used: table=exoplanets&where=*&format=JSON \n')
                result = querySend('http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&where=*&format=JSON')
                print(result, '\n')
            elif choice == '2':
                print('Query Used: table=exoplanets&format=JSON&where=pl_kepflag=1 \n')
                result = querySend('http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=JSON&where=pl_kepflag=1')
                print(result, '\n')
            elif choice == '3':
                print('Query Used: exoplanets&select=distinct%20pl_hostname&order=pl_hostname&format=JSON')
                result = querySend('http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&select=distinct%20pl_hostname&order=pl_hostname&format=JSON')
                print(result, '\n')
            elif choice == '4':
                print('Query Used: table=exoplanets&format=JSON&where=pl_tranflag=1')
                result = querySend('http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=JSON&where=pl_tranflag=1')
                print(result, '\n')
            elif choice == '5':
                print('Query Used: table=cumulative&format=JSON&where=koi_disposition%20like%20\'CANDIDATE\'')
                result = querySend("http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=cumulative&format=JSON&where=koi_disposition%20like%20'CANDIDATE'")
                print(result, '\n')
            elif choice == '6':
                print('Query Used: table=k2targets&format=JSON&where=k2_campaign=9')
                result = querySend('http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=k2targets&format=JSON&where=k2_campaign=9')
                print(result, '\n')
            elif choice == '7':
                print('Query Used: table=missionstars&format=JSON&where=st_ppnum>0')
                result = querySend('http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=missionstars&format=JSON&where=st_ppnum>0')
                print(result, '\n')
            elif choice == '8':
                print('Query Used: table=koi&format=JSON&where=kepoi_name=\'K00007.01\' OR kepoi_name=\'K00742.01\'')
                result = querySend('http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=koi&format=JSON&where=kepoi_name=\'K00007.01\' OR kepoi_name=\'K00742.01\'')
                print(result, '\n')
            elif choice == '9':
                print('Query Used: table=exoplanets&format=JSON&where=pl_discmethod%20like%20\'Microlensing\'%20and%20st_nts>0')
                result = querySend("http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=JSON&where=pl_discmethod%20like%20'Microlensing'%20and%20st_nts>0")
                print(result, '\n')
            elif choice == '10':
                print('Query Used: table=cumulative&where=koi_prad<2%20and%20koi_teq>180%20and%20koi_teq<303%20and%20koi_disposition%20like%20\'CANDIDATE\'&format=JSON')
                result = querySend("http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_prad<2%20and%20koi_teq>180%20and%20koi_teq<303%20and%20koi_disposition%20like%20'CANDIDATE'&format=JSON")
                print(result, '\n')
            elif choice.lower() == 'b' or choice == 'back':
                break

        except IndexError:
            print('Unknown Option %s' % choice)

def writeOwn():
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
        print(i, '-', "{0:30}".format(name), end='\n' if i % 10 == 4 else ' ')
    print('\n')

    category = input('Category? _> ')
    print('\n')

    print('*' * 40, 'TABLE NAMES', '*' * 40, '\n')
    for i, name in enumerate(table_lists[int(category)][1]):
        print("{0:30}".format(name), end='\n' if i % 10 == 4 else ' ')
    print('\n')
    print('*' * 93, '\n')

    table = input('Table? _> ')

    print('Gathering table columns')
    getColumns(table)

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
        data = querySend(url)
        print(data)
    elif choice.lower() == 'n':
        print('Returning all data from selected columns')
        url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=' + table + '&select=' + column + '&format=JSON'
        data = querySend(url)
        print('Query Used: ' + url + '\n')
        print(data)
    else:
        print('Input not valid')

def writeAdv():
    print('''
        For all information on how to write a basic query please see
http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#build
    ''')
    base_url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?'
    query = input('_> ')
    url = base_url + query

    query = parse_qs(query)

    columns = query.get('select')
    table = query.get('table')
    order = query.get('order')
    fmat = query.get('format')

    print('''
    Query:
        Table       =   %s
        Columns     =   %s
        Order       =   %s
        Format      =   %s
    ''' % (table, columns, order, fmat))

    data = querySend(url)
    print(data)

def querySend(url):
    pd.set_option('max_columns', 10)
    raw_data = pd.read_json(url)
    return raw_data

def getColumns(table):
    url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=' + table + '&getDefaultColumns&format=csv'
    col_names = urlopen(url).read().decode('utf8')
    col_names = col_names.split(',')
    # Thanks nedbat. I really am not sure what is going on here. I can only guess.
    for i, name in enumerate(col_names):
        print("{0:20}".format(name), end='\n' if i%10==4 else ' ')