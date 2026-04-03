import requests
import json
import os 

urlData = requests.get("https://api.nbp.pl/api/exchangerates/rates/a/EUR/")

# Daje typowo <Response ...>
# print(converter)

# Daje numer z <Response ...>
# print(converter.status_code)

data = urlData.json()
value = data["rates"][0]["mid"] # bo jest tylko jakby jedną rzecz "rates": [{...}] 
# print(value)

pln = input("To convert from PLN to EUR: ")
euro = float(pln)/float(value)
# print(f"{euro:.2f}")

plnToEuro = "converted.py"
with open(plnToEuro, "w") as file:
    file.write("euro")