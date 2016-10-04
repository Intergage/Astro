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
main.py [-h] [--pre-defined PRE_DEFINED] [--write-own WRITE_OWN]<br>
&nbsp;&nbsp;-h, --help 				+  Show this help message and exit<br>
&nbsp;&nbsp;--pre-defined PRE_DEFINED &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Pre-defined search queries<br>
&nbsp;&nbsp;--write-own WRITE_OWN &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Write your own search query<br>
&nbsp;&nbsp;--advanced-q ADVANCED_QUERY &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Create your own with no help 
\<Typing a URL\><br> 
