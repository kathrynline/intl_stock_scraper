#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:37:49 2018

@author: emilylinebarger
"""

import pandas as pd 
import numpy as np
import datetime

#What I would like this code to do: 
#1. Merge two datasets: 
#   a. A dataset of all countries compared against each other for that day
#   b. A dataset of all countries compared against themselves, over time. 

class MergeSetup():
    
    def __init__(self, country_name: str, date: str, user: str):
        self._nowstr = datetime.datetime.now().strftime("%Y-%m-%d")
        self._name = country_name
        self._date = date
        self._user = user
        
    def mergebydate(self):
        data1 = pd.read_csv("/Users/{}/Desktop/Webscraper/{}/{}_keyfigures{}.csv".format(self._user, self._date, self._name, self._date))
        df1 = pd.DataFrame(data1)
        df1['Country'] = self._name
        countries = ["Bermuda", "Brazil", "Chile", "Ecuador", "Egypt", "Israel", "Iran", "Jamaica", "Kenya", "Mauritius", "Mexico", "Pakistan", "Venezuela"]
        for country in countries:
            data2 = pd.read_csv("/Users/{}/Desktop/Webscraper/{}/{}_keyfigures{}.csv".format(self._user, self._date, country, self._date))
            df2 = pd.DataFrame(data2)
            df2['Country'] = country
            df1.append(df2)
    
    def mergebycountry(self):
        print(self._name)

run = MergeSetup("Argentina", "2018-03-04", "emilylinebarger").mergebydate()        
        
#countries = ["Argentina", "Bermuda", "Brazil", "Chile", "Ecuador", "Egypt", "Israel", "Iran", "Jamaica", "Kenya", "Mauritius", "Mexico", "Pakistan", "Venezuela"]
#
#
#for country in countries():       
#    run = MergeSetup(country, "2018-03-04", "emilylinebarger").mergebydate()

