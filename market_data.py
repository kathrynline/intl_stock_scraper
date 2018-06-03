#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:38:40 2018

@author: emilylinebarger
"""
import os
import csv
import datetime  
import requests
from bs4 import BeautifulSoup

class CountryData():
    
    def __init__(self, country_name: str, url: str):
        self._nowstr = datetime.datetime.now().strftime("%Y-%m-%d")
        if os.path.exists("/Users/emilylinebarger/Desktop/Webscraper/{}".format(self._nowstr)):
            pass
        else:
            os.mkdir("/Users/emilylinebarger/Desktop/Webscraper/{}".format(self._nowstr))
        self._output_dir = "/Users/emilylinebarger/Desktop/Webscraper/{}".format(self._nowstr)
            
        self.name = country_name
        self.url = url
        self._response = requests.get(self.url)
        self._soup = BeautifulSoup(self._response.content, "lxml")
            
        self.get_key_figures()
        self.get_latest_figures()
        
    def get_key_figures(self):
        table = self._soup.find(class_ = 'table table-small no-margin-bottom')
        
        list_of_rows=[]
        for row in table.findAll('tr')[1:]:
            list_of_cells = []
            for cell in row.findAll('td'):
                text = cell.text
                list_of_cells.append(text)
            list_of_rows.append(list_of_cells)
         
        with open('{}/{}_keyfigures{}.csv'.format(self._output_dir, self.name, self._nowstr),'w') as outfile:
            writer=csv.writer(outfile)
            writer.writerow(["Statistic", "30 Days", "90 Days", "250 Days"])
            writer.writerows(list_of_rows)
    
    def get_latest_figures(self):
        table2 = self._soup.find(class_ = 'table-responsive drop-up-enabled')

        list_of_rows=[]
        for row in table2.findAll('div')[1:]:
            list_of_rows.append(row)
            
        with open('{}/{}_latestfigures{}.csv'.format(self._output_dir, self.name, self._nowstr),'w') as outfile:
            writer=csv.writer(outfile)
            writer.writerows(list_of_rows)

countries = {
            "Argentina": 'http://markets.businessinsider.com/index/merval_25', 
            "Bermuda":   'http://markets.businessinsider.com/index/bsx', 
            "Brazil":    'http://markets.businessinsider.com/index/bovespa', 
            "Chile":     'http://markets.businessinsider.com/index/ipsa',
            "Ecuador":   'http://markets.businessinsider.com/index/bvq', 
            "Egypt":     'http://markets.businessinsider.com/index/egx30',
            "Israel":    'http://markets.businessinsider.com/index/ta_100',
            "Iran":      'http://markets.businessinsider.com/index/tepix',
            "Jamaica":   'http://markets.businessinsider.com/index/jse_index', 
            "Kenya":     'http://markets.businessinsider.com/index/nse', 
            "Mauritius": 'http://markets.businessinsider.com/index/semdex',
            "Mexico":    'http://markets.businessinsider.com/index/ipc', 
            "Pakistan":  'http://markets.businessinsider.com/index/kse_100', 
            "Venezuela": 'http://markets.businessinsider.com/index/ibc'
        }

for name, url in countries.items():
        CountryData(name, url)



    