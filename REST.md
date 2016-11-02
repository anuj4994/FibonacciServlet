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
  
