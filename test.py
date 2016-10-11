from prettytable import PrettyTable
import pandas

table_lists = [('Confirmed Planets', ['exoplanets', 'multiexopars']),
               ('KOI (Cumulative)', ['cumulative', 'q1_q17_dr24_koi', 'q1_q16_koi', 'q1_q12_koi', 'q1_q8_koi', 'q1_q6_koi']),
               ('Threshold-Crossing Events', ['q1_q17_dr25_tce', 'q1_q17_dr24_tce', 'q1_q16_tce', 'q1_q12_tce']),
               ('K-Stellar Properties', ['keplerstellar', 'q1_q17_dr25_stellar', 'q1_q17_dr24_stellar', 'q1_q16_stellar', 'q1_q12_stellar', 'keplertimeseries', 'keplernames']),
               ('KELT Time Series', ['kelttimeseries', 'EG: &kelt_field=N02']),
               ('SuperWASP Time Series', ['superwasptimeseries', 'EG: &tile=tile168060  OR  &sourceid=1SWASP J191645.46+474912.3']),
               ('K2', ['k2targets', 'k2candidates', 'k2names']),
               ('Mission Stars', ['missionstars', 'mission_exocat'])]


table_frame = PrettyTable(['#', 'Name'])
i = 0
for x, y in table_lists:
    i += 1
    table_frame.add_row([i, x])

print(table_frame)









'''
import click

@click.group()
def click_grp():
    pass

@click_grp.command(name='-b')
@click.option('--table', type=(str))
@click.option('--column', type=(str))
@click.option('--con', type=(str))
def basic(table, column, con):
    print(
    Basic:-
        Table:      %s
      Columns:      %s
    Condition:      %s
     % (table, column, con))

click_grp()


arg_help = [('Pre-defined Queries: ', ['[--pre-defined]', 'A list of queries taken from http://exoplanetarchive.ipac.caltech.edu/docs/API_queries.html']),
            ('Build your own query: ', ['[--write-own]', 'Use a \'wizard\' style module to help create queries']),
            ('Write advanced query: ', ['[--write-adv]', 'A prompt that will allow you to write your own query from scratch. MUST KNOW API SYNTAX'])]



if __name__ == '__main__':
    try:
        if sys.argv[1] == '--pre-defined':
            print(INTRO)
            modules.preDefined()
        elif sys.argv[1].lower() == '-h' or sys.argv[1].lower() == '-help':
            for arg_name, arg_options in arg_help:
                print('\t', arg_name, arg_options[0], '\n\t\t', arg_options[1], '\n')
        elif sys.argv[1] == '--write-own':
            print(INTRO)
            modules.writeOwn()
        elif sys.argv[1] == '--write-adv':
            print(INTRO)
            modules.writeAdv()
        else:
            print('Unknown Arg')
    except:
        print(INTRO)
        main()



print('*' * 40, ' CATEGORY ', '*' * 40, '\n')
for i, name in enumerate(temp):
    print(i, '-', "{0:30}".format(name), end='\n' if i % 10 == 4 else ' ')
print('\n')
print('*' * 93, '\n')


print('*' * 40, 'TABLE NAMES', '*' * 40, '\n')
for i, name in enumerate(table_lists[int(category)][1]):
    print("{0:30}".format(name), end='\n' if i % 10 == 4 else ' ')
print('\n')
print('*' * 93, '\n')


# Thanks nedbat. I really am not sure what is going on here. I can only guess.
print('\n')
print('*' * 40, ' COLU NAMES ', '*' * 40, '\n')
for i, name in enumerate(col_names):
    print("{0:20}".format(name), end='\n' if i%10==4 else ' ')
print('\n')
print('*' * 93, '\n')


shorten those padding lines to l.extend(('' for _ in range(total-len(l))))

'''

'''
    pl_len = len(pl_list)
    st_len = len(st_list)
    leftover_len = len(leftover)

    total = max(pl_len, st_len, leftover_len)

    if pl_len <= total:
        x = total - pl_len
        for i in range(x):
            pl_list.append('')
    if st_len <= total:
        x = total - st_len
        for i in range(x):
            st_list.append('')
    if leftover_len <= total:
        x = total - leftover_len
        for i in range(x):
            leftover.append('')


    col_frame = PrettyTable()
    col_frame.add_column('PL', pl_list, 'l')
    col_frame.add_column('ST', st_list, 'l')
    col_frame.add_column('Oth', leftover, 'l')
    print(col_frame)
'''