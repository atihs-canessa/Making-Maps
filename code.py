
import json
import numpy as np
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
import requests

source = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita').text
soup  = BeautifulSoup(source, 'lxml')
body = soup.find('body')
table = body.find('table')
tablemain = table.find('table', class_ ='wikitable nowrap sortable mw-datatable')

countrylist = []
for data in tablemain.find_all('tbody'):
    rows = data.find_all('tr')
    rows.pop(0)
    for row in rows:
        country = row.find('a')
        countrylist.append(country)


countrynames = []
for x in countrylist:
    names = x.get('title')
    countrynames.append(names)
#This works!^



#Now i need some data to plot for the countries
#Use "total"


total = []
for data in tablemain.find_all('tbody'):
    rows = data.find_all('tr')
    rows.pop(0)
    for row in rows:
        tot = row.find_all('td') [1]
        total.append(tot.text)


#Here i am taking the list called "total" and turning each of its elements from strings to floating points
floatal = []
for i in total:
    i = float(i)
    floatal.append(i)







#combine two lists to make a dictionary of key value pairs
# THIS >> DIDNT WORK BECAUSE PX NEEDS THE DICTIONARY IN THE FORM OF A K/V PAIR OF TWO LISTS I.E. "KEY":VALUE.   dictionary = dict(zip(countrynames, floatal))
countries = tuple(countrynames)
dictionary = {'Countries':countrynames,'Score':floatal}

df = pd.DataFrame(dictionary)
fig = px.bar(df, x="Countries",y="Score")
fig.show()

