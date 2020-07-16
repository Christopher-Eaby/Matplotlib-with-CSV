# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jul  9 10:02:09 2020
@author: Chris
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as sql

#intalizing the rows, columns and data for the dataframe
dat = ['Simba', 'Lays'], ['Coke', 'Fanta'], ['Cadbury', 'Tex'], ['Pepper Steak', 'Chicken'], ['Pear', 'Apple', 'Orange'], ['Vanilla', 'Choclate'], ['Spinach', 'Cabbage']
rows = ['Chips', 'Cooldrinks', 'Chocolates', 'Pies', 'Fruit', 'Cupcakes', 'Veggies']
column = ['Item 1', 'Item 2', 'Item 3']
     
#creates the dataframe
df = pd.DataFrame(data = dat, index = rows, columns = column)
#saves all the data from the dataframe to a csv file
df.to_csv("Items1.csv")
#creates a connection between the database and the python file
connection = sql.connect("sprint3.db") 
#allows the python file to execute SQL queries
crsr = connection.cursor() 

#function to create a new table if there isn't already one
def create_tables(): 
    crsr.execute('CREATE TABLE IF NOT EXISTS Items(Item1 TEXT, Item2 TEXT, Item3 TEXT)')
create_tables()

def data_entry(item1, item2, item3): 
    crsr.execute("INSERT INTO Items (Item1, Item2, Item3) VALUES(?, ?, ?)", (item1, item2, item3))  
    connection.commit() 
    
for x in (df.index):
    data_entry(df['Item 1'][x], df['Item 2'][x], df['Item 3'][x])

#imports the info from the csv files and saves them into a list in the data variables
data1 = np.genfromtxt("stocks.csv", delimiter=",", names = ["Type", "chips", "cooldrinks", "pies", "fruit", "cupcakes", "veggies"])
data = np.genfromtxt("Items1.csv", delimiter=",", names = ["Type", "1", "2", "3",])
#labels the different axes and changes the color and font size
plt.xlabel('Week', {'color':'red', 'fontsize':15})
plt.ylabel('Stock', {'color':'red', 'fontsize':15})
#changes the angle of the text next to increments of the plot
plt.xticks(rotation = 35, color='blue', size=13)
plt.yticks(rotation = 35, color='blue', size=13)
#plots all the stock levels of the items with butllets and key in the top right
plt.plot(data1['chips'], 'o-', label = 'chips')
plt.plot(data1['cooldrinks'], 'o-', label = 'cooldrinks')
plt.plot(data1['pies'], 'o-', label = 'pies')
plt.plot(data1['fruit'], 'o-', label = 'fruit')
plt.plot(data1['cupcakes'], 'o-', label = 'cupcakes')
plt.plot(data1['veggies'], 'o-', label = 'veggies')
#creates a key for the top right of the graph
plt.legend(loc = "upper right")
