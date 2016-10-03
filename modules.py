import pandas as pd
from urllib.request import urlopen

from collections import OrderedDict

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
