# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:44:26 2022

@author: Johnny Tsao
"""
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

# Get today's date
start_date = datetime.today()

# Generate a list of date strings for the next 10 days
date_strings = [f"?date={(start_date + timedelta(days=i)).strftime('%m/%d/%y')}" for i in range(10)]
dir_path = os.path.dirname(os.getcwd())

with open(dir_path+"/data.txt","w") as textfile:
    for date_string in date_strings:
        url = 'https://www.utrecsports.org/facilities/facility-schedules/' + date_string
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        tables = soup.find_all("table")
        rows = []
        for row in tables[2].findAll("tr"):
            cols = []
            for col in row.findAll("td"):
                cols.append(col.text)
            rows.append(cols)
        days = []
        gym = ""
        data = []

        for cols in rows:
            if(len(cols) == 1):
                title = cols[0]
                if(len(title) < 10):
                    gym = title
                else:
                    days.append(title)
            if(len(cols) == 3):
                string = cols[2]
                elem =string.split(" ")
                search_word = 'Informal Badminton'
                if(search_word in string):
                    print(days[-1], cols[1])
                    print(gym, cols[0])
                    data.append([days[-1] + " " + cols[1],
                                gym  + " " + cols[0]])
                    textfile.write("{:25s} {:15s} {:5s} {:15s} \n"\
                                .format(days[-1], cols[1], gym,cols[0]))
                    print(" ")
                



############ Obsolete after spring 2025 ############
 
# import requests
# import urllib.request
# import time
# from bs4 import BeautifulSoup
# import numpy as np
# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))

# url = 'https://www.utrecsports.org/facilities/facility-schedules'
# response = requests.get(url)

# soup = BeautifulSoup(response.content,"html.parser")
# tables = soup.find_all("table")
# print(tables)
# rows = []
# for row in tables[1].findAll("tr"):
#     cols = []
#     for col in row.findAll("td"):
#         cols.append(col.text)
#     rows.append(cols)
    
# days = []
# gym = ""
# data = []

# textfile = open(dir_path+"/data.txt","w")

# for cols in rows:
#     if(len(cols) == 1):
#         title = cols[0]
#         if(len(title) < 10):
#             gym = title
#         else:
#             days.append(title)
#     if(len(cols) == 3):
#         string = cols[2]
#         elem =string.split(" ")
#         search_word = 'Informal Badminton'
#         if(search_word in string):
#             print(days[-1], cols[1])
#             print(gym, cols[0])
#             data.append([days[-1] + " " + cols[1],
#                          gym  + " " + cols[0]])
#             textfile.write("{:25s} {:15s} {:5s} {:15s} \n"\
#                            .format(days[-1], cols[1], gym,cols[0]))
#             print(" ")
            
# textfile.close()
            
