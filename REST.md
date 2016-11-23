I have created RESTful webservice in python. This service can generate fibonacci series till number passed, can find factorial of 
a number and can tell number is prime or not.



1. To generate fibonacci: 
    url: http://54.70.113.238:5000/fibonacci/5
    parameter : Enter the number of digits wanted in the series in the place of 5 (i.e. http://54.70.113.238:5000/fibonacci/<input>)
    output : {"fibonacci": "0, 1, 1, 2, 3"}
    
2. To find Factroial :
    url : http://54.70.113.238:5000/factorial/5
    parameter : Enter the number of which you want to fing factorial in place of 5. (i.e.http://54.70.113.238:5000/factorial/<input>)
    output : {"factorial": 120}
    
3. To Check number is prime or not :
    url : http://54.70.113.238:5000/checkPrime/5
    parameter : Enter the number which you want to check in the place of 5 (i.e. http://54.70.113.238:5000/checkPrime/<input>)
    output : {"prime": "True"}
  
Added new service which can tell the distance between 2 places and tells how much time it will take to drive there. In In this service I have used google's distance matrix api, which gives the output. After that I parsed the output given by google and return only what is most importannt.

4. To get distance between two places and time taken to travel :
    url : http://54.70.113.238:5000/getDistance/cincinnati/chicago
    parameter : Enter from city and to city, order doesn't matter because we just want distance and time. parameter are in url itself i.e.(http://54.70.113.238:5000/getDistance/(from city)/(to city))
    output : {"duration": "4 hours 35 mins", "distance": "294 mi"}
