import pandas as pd
from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs
from prettytable import PrettyTable
import json

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
        # If I want to add the old "Query Used: <Query>" line before the result is printed
        # Change the values to lists and add the string as index 2.
        # Index below as needed.
        MENU = {
            1: ('All confirmed planets and columns', 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&where=*&format=JSON'),
            2: ('Confirmed planets in the Kepler field (default columns)', 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=JSON&where=pl_kepflag=1'),
            3: ('Stars known to host exoplanets listed in ascending order', 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&select=distinct%20pl_hostname&order=pl_hostname&format=JSON'),
            4: ('Confirmed planets that transit their host stars (default columns)', 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=JSON&where=pl_tranflag=1'),
            5: ('A current list of non-confirmed planet candidates', "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=cumulative&format=JSON&where=koi_disposition%20like%20'CANDIDATE'"),
            6: ('K2 targets from campaign 9', 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=k2targets&format=JSON&where=k2_campaign=9'),
            7: ('Confirmed planets in the Mission Star list', 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=missionstars&format=JSON&where=st_ppnum>0'),
            8: ('All default parameters for one particular KOI or another', 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=koi&format=JSON&where=kepoi_name=\'K00007.01\' OR kepoi_name=\'K00742.01\''),
            9: ('All microlensing planets with time series', "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=JSON&where=pl_discmethod%20like%20'Microlensing'%20and%20st_nts>0"),
            10: ('All planetary candidates smaller than 2Re with equilibrium temperatures between 180-303K', "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_prad<2%20and%20koi_teq>180%20and%20koi_teq<303%20and%20koi_disposition%20like%20'CANDIDATE'&format=JSON"),
            0: ('Main Menu', None)
        }

        options = sorted(MENU.keys())
        for opt in options:
            print('\t', opt, '\t', MENU[opt][0])
        choice = input('_> ')
        if choice == '0':
            break
        else:
            result = querySend(MENU.get(int(choice))[1])
            print(result, '\n')


def writeOwn():
    print('''
                                    QWizard
    ----------------------------------------------------------------------------
               For all table, column and data names please see
    http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data

            I have tried to make it as easy as I can to create
            your own query without learning the correct syntax

            Tables are split into categories for ease of use.
            Please select what category you'd like to explore.\n\n
                    ''')
    # Print out Categories in a table format
    table_frame = PrettyTable(['#', 'Category'])
    i = 0
    for x, y in table_lists:
        table_frame.add_row([i, x])
        i += 1
    print(table_frame, '\n')

    category = input('Category? _> ')

    # Prints out Tables from selected category
    col_frame = PrettyTable(['', 'Tables'])
    i = 0
    for x in table_lists[int(category)][1]:
        col_frame.add_row(['', x])
        i += 1
    print(col_frame)

    # Select table
    print('''
    Now you need to select a table
    Each table holds certain data
    Use the URL in module description
    To see what each table offers
    ''')
    table = input('Table? _> ')

    # Gets Table columns from API
    print('Gathering table columns')
    getColumns(table)

    # Select what coloumns you want to grab data from
    print('''
    These are the columns for the selected table
    You need to select what columns to return
    You can select a single column or multiple
    Separate them with a comma(,)
    ''')
    column = input('Column(s)? _> ')

    # Check if user wants arguments in the query
    print('''
    Now we can set arguments for your query.
    You will need to know basic SQL (SoQL(?))
    http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#syntax
                    ''')
    choice = input('Write Arguments? y/n_> ')

    if choice.lower() == 'y':
        # If yes, take argument string and build URL. Send to querySend()
        argz = input('Arguments _> ')
        url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=' + table + '&select=' + column + '&where=' + argz + '&format=JSON'
        data = querySend(url)
        print(data)
    elif choice.lower() == 'n':
        # If no, return all data from table and columns selected.
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
                        b or back for Main Menu
    ''')
    base_url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?'
    query = input('_> ')
    if query.lower() == 'b' or query.lower() == 'back':
        return
    else:
        url = base_url + query

        query = parse_qs(query)

        columns = query.get('select')
        table = query.get('table')
        order = query.get('order')
        fmat = query.get('format')

        print('''
        Query:
              Table   =   %s
            Columns   =   %s
              Order   =   %s
             Format   =   %s
        ''' % (table, columns, order, fmat))

        data = querySend(url)
        print(data)


def querySend(url):
    raw_data = pd.read_json(url)
    return raw_data


def getColumns(table):
    url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=' + table + '&getAllColumns&format=csv'
    col_names = urlopen(url).read().decode('utf8')
    col_names = col_names.split(',')

    pl_list = []
    st_list = []
    ot_list = []

    for name in col_names:
        if 'pl_' in name:
            pl_list.append(name)
        elif 'st_' in name:
            st_list.append(name)
        elif name:
            ot_list.append(name)

    longest_col = max(len(pl_list), len(st_list), len(ot_list))

    def data_append(l, list_len):
        for idx in range(list_len):
            try:
                l[idx]
            except:
                l.append('')

    #[data_append(_, longest_col) for _ in (pl_list, st_list, ot_list)]

    data_append(pl_list, longest_col)
    data_append(st_list, longest_col)
    data_append(ot_list, longest_col)

    col_frame = PrettyTable()
    col_frame.add_column('PL', pl_list, 'l')
    col_frame.add_column('ST', st_list, 'l')
    col_frame.add_column('Oth', ot_list, 'l')

    print(col_frame)

def planetOverview():
    print('''
            Planet Overview
    Show basic planet information
          Enter a planet name.
    ''')

    planet = input('_> ')
    url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&select=pl_hostname,pl_letter,pl_discmethod,pl_orbper,pl_orbsmax,pl_orbincl,pl_bmassj,pl_radj,pl_dens,ra,dec&where=pl_name%20like%20'" + planet + "'&format=json"
    url = url.replace(' ', '%20')

    response = urlopen(url).read().decode('utf-8')
    data = json.loads(response)
    data = data[0]

    print('''
    General Info for %s:
        Planet Letter:                  %s
        Host Star:                      %s
        Discovery Method:               %s

    Orbit Info for %s:
        Orbit Period (E-Days):          %s
        Orbit Semi-Major Axis (AU)      %s
        Orbit Inclination:              %s

    Planet Size Info for %s
        Planet Mass (Unit: Jupiter):    %s
        Planet Radius (Unit: Jupiter):  %s
        Planet Density:                 %s

    %s Location in sky:
        Right Ascension:                %s
        Declination:                    %s
       ''' % (planet, data.get('pl_letter'), data.get('pl_hostname'), data.get('pl_discmethod'), planet, data.get('pl_orbper'), data.get('pl_orbsmax'), data.get('pl_orbincl'), planet, data.get('pl_bmassj'), data.get('pl_radj'), data.get('pl_dens'), planet, data.get('ra'), data.get('dec')))
