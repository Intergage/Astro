# Astro
##Random API Search tool thingo. 

#### API Used: http://exoplanetarchive.ipac.caltech.edu
API:                        http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data<br>
Pre-generate API Queries:   http://exoplanetarchive.ipac.caltech.edu/docs/API_queries.html<br>
Format control:             &format=JSON<br>
Get Columns for table:      table=exoplanets&getDefaultColumns<br>


Example:<br>
    \<Standard URL\>nph-nstedAPI?table=\<TABLENAME\>&select=\<COLUMN NAMES,CAN HAVE MANY\><br>
    
    
#### Arugments
`  -h, --help            show this help message and exit
  --pre-defined PRE_DEFINED
                        Pre-defined search queries
  --write-own WRITE_OWN
                        Write your own query
`
