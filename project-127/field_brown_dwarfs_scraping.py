import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(start_url)

soup = BeautifulSoup(page.text,"html.parser")

field_dwarf_table = soup.find_all("table", {"class","wikitable sortable"})

total_table = len(field_dwarf_table)

Empty_list = []

table_rows = field_dwarf_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    Empty_list.append(row) 

Star_Names = []
Distance = []
Mass = []
Radius = []

dwarfs_data = []

for i in range(1,len(Empty_list)):
    Star_Names.append(Empty_list[i][0])
    Distance.append(Empty_list[i][5])
    Mass.append(Empty_list[i][7])
    Radius.append(Empty_list[i][8])
    
headers = ['Star_name','Distance','Mass','Radius']  
   
star_dwarf_1 = pd.DataFrame(list(zip(Star_Names,Distance,Mass,Radius,)), columns=['Star_Names','Distance','Mass','Radius'])

star_dwarf_1.to_csv('scraped_data_2.csv',index=True, index_label="id")

