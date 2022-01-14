'''
Created on 

Course work: 

@author: vedha

Source:
    
'''
# Import necessary modules

from flask import Flask,render_template,request
import json
import random

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def start():


    return render_template('index.html')

@app.route('/get-cities', methods=["POST"])
def get_cities():

    cities =[
        "Airdrie",
        "Beaumont",
        "Nova Scotia",
        "Ontario",
        "Quebec",
        "Leduc",
        "Alberta",
        "British Columbia",
        "Manitoba",
        "New Brunswick"
    ] 

    countries = [
        "Anguilla",
        "Bahamas",
        "Burundi",
        "Chile",
        "Denmark",
        "Ecuador",
        "Faroe Islands",
        "Greece",
        "Greenland",
        "Hong Kong"
    ]

    addr    = request.values.get("addr")
    c_code  = request.values.get("code")

    # print (addr, c_code)

    random_city = random.choice(cities)
    random_c_code = random.choice(countries)


    return render_template('index.html', city = random_city, country = random_c_code)


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)