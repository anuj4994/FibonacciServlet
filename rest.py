# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:24:05 2016

@author: Anuj Shah
"""

from flask import Flask
from flask_restful import Resource, Api
from flask import Response
from flask import request
import xml.etree.ElementTree as ET
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
         
class apiRSDL(Resource):
    def get(self):
        y = '<?xml version="1.0" encoding="UTF-8" ?><rsdl><description>This webservice lets you find the fibonacci series of the number which user has passed. User can also find facotial of the number and user can check weather the passed number is prime or not. This webservice will accept input as a integer values and gives ouput in JSON format. User has to pass parameter in the url itself. This web service uses path parameters.</description><version major="1" minor="0" build="0" revision="12" /><links><link rel="get" href="/fibonacci/number"><request><url><parameters_set><parameter type="xs:int" required="true"><name>Number</name><value>Number of element wanted in fibonacci series.</value></parameter></parameters_set></url></request><response><type>JSON containing result</type></response></link><link rel="get" href="/factorial/number"><request><url><parameters_set><parameter type="xs:int" required="true"><name>number</name><value>Number of which the factorial is needed by user.</value></parameter></parameters_set></url></request><response><type>JSON containing result</type></response></link><link rel="get" href="/checkPrime/number"><request><url><parameters_set><parameter type="xs:int" required="true"><name>number</name><value>Number which user wants to check weather its prime or not.</value></parameter></parameters_set></url></request><response><type>JSON containing result</type></response></link></links></rsdl>'
        rsdl = request.args.get('rsdl')
        if(rsdl == ""):
            x = 'rsdl.xml'
            #y = ET.parse(x)
            
            return Response(y, mimetype='text/plain')        #print(BeautifulSoup(x, "xml").prettify())         
        return Response(y, mimetype='text/xml') 
        
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
api.add_resource(apiRSDL, '/api')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
