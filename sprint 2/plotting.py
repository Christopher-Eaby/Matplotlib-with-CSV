# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jul  9 10:02:09 2020
@author: Chris
"""

#import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import MySQLdb

#intalizing the rows, columns and data for the dataframe
dat = ['Simba', 'Lays'], ['Coke', 'Fanta'], ['Cadbury', 'Tex'], ['Pepper Steak', 'Chicken'], ['Pear', 'Apple', 'Orange'], ['Vanilla', 'Choclate'], ['Spinach', 'Cabbage']
rows = ['Chips', 'Cooldrinks', 'Chocolates', 'Pies', 'Fruit', 'Cupcakes', 'Veggies']
column = ['Item 1', 'Item 2', 'Item 3']
     
#creates the dataframe
df = pd.DataFrame(data = dat, index = rows, columns = column)
#saves all the data from the dataframe to a csv file
df.to_csv("Items1.csv")

"""
My MySQL didn't want to install correctly and I tried everything, so I just found 
another way and commented out the things that didn't work

mydb = MySQLdb.connect(host='localhost', user='root', passwd='', db='dbdb')
cursor = mydb.cursor()

csv_data = csv.reader(file('Items1.csv'))
csv_data1 = csv.reader(file('stocks.csv'))
"""

#imports the info from the csv files and saves them into a list in the data variables
data1 = np.genfromtxt("stocks.csv", delimiter=",", names = ["Type", "chips", "cooldrinks", "pies", "fruit", "cupcakes", "veggies"])
data = np.genfromtxt("Items1.csv", delimiter=",", names = ["Type", "1", "2", "3",])
print(data1)
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