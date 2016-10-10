import click

@click.group()
def click_grp():
    pass

@click_grp.command(name='-b')
@click.option('--table', type=(str))
@click.option('--column', type=(str))
@click.option('--con', type=(str))
def basic(table, column, con):
    print('''
    Basic:-
        Table:      %s
      Columns:      %s
    Condition:      %s
    ''' % (table, column, con))

click_grp()


'''

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
'''