# Astro
##Random API Search tool thingo. 

#### API Used: http://exoplanetarchive.ipac.caltech.edu
API:                        http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data

Pre-generate API Queries:   http://exoplanetarchive.ipac.caltech.edu/docs/API_queries.html

Format control:             &format=JSON

Get Columns for table:      table=exoplanets&getDefaultColumns


Example:

    <Standard URL>nph-nstedAPI?table=<TABLENAME>&select=<COLUMN NAMES,CAN HAVE MANY>
    
    
#### Arugments
main.py [-h] [--pre-defined PRE_DEFINED] [--write-own WRITE_OWN]
  
  -h, --help                                      Show this help message and exit
  
  --pre-defined PRE_DEFINED                       Pre-defined search queries
  
  --write-own WRITE_OWN                           Write your own search query
  
  --advanced-q ADVANCED_QUERY                     Create your own with no help <Typing a URL> 
