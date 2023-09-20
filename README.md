# csv_to_sql
This is a script that reads from weather_newyork.csv (using the CSV module), selects the date, mean_temp, precip, and events columns, and inserts them row-by-row into the table I created, weather_newyork.

Ex. from terminal...
Number of row in weather_newyork table: 366

Ex. from db...
```
sqlite> SELECT * FROM weather_newyork;
date      mean_temp  precip  events       
--------  ---------  ------  -------------
1/1/16    38         0.0                  
1/2/16    36         0.0                  
1/3/16    40         0.0                  
1/4/16    25         0.0                  
1/5/16    20         0.0                  
1/6/16    33         0.0                  
1/7/16    39         0.0                  
1/8/16    39         0.0                  
1/9/16    44                 Rain         
1/10/16   50         1.8     Rain         
1/11/16   33         0.0                  
1/12/16   35                              
1/13/16   26         0.0                  
1/14/16   30                              
1/15/16   43                              
1/16/16   47         0.24    Rain         
1/17/16   36         0.05    Fog-Snow     
1/18/16   25                 Snow         
1/19/16   22         0.0
```            
