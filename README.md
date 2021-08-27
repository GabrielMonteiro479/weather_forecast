# Full Stack Code Assesment Challenge - Backend
Author: Gabriel Monteiro Araujo da Silva
DevGrid Back-End Coding Challenge
Position: Python Flask Backend Developer

Python Version: 3.9.6
Flask Version: 2.0.1

Objective
    - Design and build an application that for a given city name, collects data from the Open Weather API, caches it for some
      configurable time and returns it as a JSON object. Also returns a configurable number of last searched cities.
      
First of all, you need to install all the requirements for this application. Execute command below on terminal:
      pip install -r requirements.txt
      
Then, to run the application, just execute the main file
      python run.py
      
The enviroment is set as 'dev'. It activates debugging mode in order to facilitate debugging and running some tests.
Some useful information are being displayed on terminal when you use the available paths

Main path: http://127.0.0.1:5000/

1) To get the cache data for the specified city name or to fetch it from the Open Weather API, caches and returns the results, the path is:
           http://127.0.0.1:5000/weather/<city_name>
           
           Example: http://127.0.0.1:5000/weather/chicago
           
2) To get all the cached cities, up to the latest n entries (configurable) or max_number (if specified), the path is:
           http://127.0.0.1:5000/weather/max=<max_number>
           
           Example: http://127.0.0.1:5000/weather/max=4    or
                    http://127.0.0.1:5000/weather/max=
           
   If max_number is not specified or it is attributed as zero, maximum of 5 entries by default is displayed.
   
   
   
OBS: 
    - Cache lives for 5 minutes. After that, everything is deleted.
    - I noticed in the challenge description that the path for item 2 was mistyped. That being said, I replaced the "?" character for "/" and it worked.

Recommendations: 
    a) First of all, run the first path above in order to cache different cities or to display weather forecast informations about a specified cached city;
    b) You can cache as many data you want;
    c) After doing "a" and "b", then run the second path above to display the latest n entries or max_number.
    
  
