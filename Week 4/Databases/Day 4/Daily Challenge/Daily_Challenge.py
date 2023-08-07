import sqlite3
import requests
import json
import pprint

countries_api = requests.get('https://restcountries.com/v3.1/all')

countries = countries_api.json()

for country_data in countries:
    name = country_data['name']['common']
    flag = country_data['flag']
    print(flag)