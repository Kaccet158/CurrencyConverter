import os
import json
import requests
from datetime import datetime

# Covnverter class
class Converter:
    def __init__(self, pln, rate):
       self.toEuro = float(pln)/float(rate)

# Using requests 
url = "https://api.nbp.pl/api/exchangerates/rates/a/EUR/"
data = requests.get(url).json() # Data from API is JSON format
rateCurrent = data["rates"][0]["mid"]

# Getting PLN data to convert
pln = input("")
convertData = Converter(pln, rateCurrent)
euro = convertData.toEuro
# print(convertData.toEuro)

# Current date and time
dateTime = datetime.now()

# Save convertData to plnToEuro.txt
file = "plnToEuro.txt"
with open(file, "w", encoding = "utf-8" ) as file:
    file.write(f"{euro:.2f}\n{dateTime.strftime("%d.%m.%Y %H:%M")}")