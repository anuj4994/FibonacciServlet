# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:24:05 2016

@author: arpit51187
"""

from flask import Flask
from flask_restful import Resource, Api
import math

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
        
class generateFact(Resource):
    def get(self,number):
         result = 1
         for i in xrange(2, number + 1):
             result *= i
         return {"factorial":result}
         
class checkPrime(Resource):
    def get(self,number):
         if number == 2:
             return {"prime" : "True"}
         if number % 2 == 0 or number <= 1:
             return {"prime" : "False"}
    
         sqr = int(math.sqrt(number)) + 1
    
         for divisor in range(3, sqr, 2):
             if number % divisor == 0:
                 return {"prime" : "False"}
         return {"prime" : "True"}
        
class generateFibo(Resource):
    def get(self,number):
       
       result = "0, 1"
       a = 0
       b = 1
       i = 0
       while i < number - 2:
           i = i + 1
           tmp_var = b      
           b = a + b        
           a = tmp_var   
           result = result + ", " + str(b)  
            # print(a)
       return {"fibonacci" : result}

api.add_resource(HelloWorld, '/')
api.add_resource(generateFibo, '/fibonacci/<int:number>')
api.add_resource(generateFact, '/factorial/<int:number>')
api.add_resource(checkPrime, '/checkPrime/<int:number>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')