# Astro
##Random API Search tool thingo. 
**API Used:**			 http://exoplanetarchive.ipac.caltech.edu<br>
**API Doco:**                    http://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data<br>
**Pre-generate API Queries:**    http://exoplanetarchive.ipac.caltech.edu/docs/API_queries.html<br>
**Format control:**              *&format=JSON*<br>
**Get Columns for table:**       *table=exoplanets&getDefaultColumns*<br>


**Example:<br>**
   *\<Standard URL\>nph-nstedAPI?table=\<TABLENAME\>&select=\<COLUMN NAMES,CAN HAVE MANY\>*<br>
    
    
#### Arguments Table
| Switch	| Use	|
|---		|---	|
|-h		|Show the help message|
|--pre-defined	|Pre-defeined search queries|
|--write-own	|Write your own query using a wizard|
|--write-adv	|Write your own query as a string|
