# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:29:59 2022

@author: GOKULNATH
"""
# Implementation of pandas function
import pandas as pd 
# Implementation of Matplotlib function
import matplotlib.pyplot as plt
# implementation of numpy function
import numpy as np 

# To define a function use def 
def Bar_plot(filename):
    # use skiprows if you want to skip headers
    x=pd.read_csv(filename,skiprows=4)
    x=x.drop(["Country Code","Indicator Name","Indicator Code"],axis=1)
    # To print new data
    print(x)
    
    #To replace Null values with specified value
    bar1=x.fillna(0)
    print(bar1)
    
    # To select values in a specific row
    bar2=(bar1.apply(lambda row: row[bar1["Country Name"].
                        isin(['Switzerland','Denmark','Argentina','India'])]))
    print(bar2)
    plt.figure()
    bar2.plot(x="Country Name",
              y=["2010","2011","2012","2013","2015"],kind="bar")
    
    # set label location in x-axis
    plt.xticks(rotation = 0)
    # depicting the visualization
    plt.ylabel('Land area')
    # displaying the title
    plt.title("Population")
    # to display all elements of a graph
    plt.legend(title='Year',loc='upper center',bbox_to_anchor=(1.10, 0.6))
    #To show the plot
    plt.show()    
    
Bar_plot(r"E:\Population growth\Population growth.csv")    

def Bar_plot2(filename): # to define a function using def 

    # use skiprows if you want to skip headers
    y=pd.read_csv(filename,skiprows=4)
    # to drop certain columns and rows use drop function
    y=y.drop(["Country Code","Indicator Name","Indicator Code"],axis=1)
    # to print new data
    print(y)
    
    #To replace Null values with specified value
    bar1=y.fillna(0)
    print(bar1)
    # To select values in a specific row
    bar2=(bar1.apply(lambda row: row[bar1["Country Name"].
                        isin(['Switzerland','Denmark','Argentina','India'])]))
    print(bar2)
    plt.figure()
    
    bar2.plot(x="Country Name",
              y=["2010","2011","2012","2013","2015"],kind="bar")
    # to set label location in x-axis
    plt.xticks(rotation = 0)
    plt.ylabel('Land area')
    
    # displaying the title
    plt.title("Forest")
    plt.legend(title='Year',loc='upper center',bbox_to_anchor=(1.10, 0.6))
    plt.show()
      
Bar_plot2(r"E:\Forest area\Forest area.csv")    


def line_plot(filename):
    # use skiprows if you want to skip headers
    line=pd.read_csv(filename,skiprows=4)
    print(line)
    
    # to select specific columns in data set
    country1= line.iloc[46,48:52]
    country2= line.iloc[64,48:52]
    country3= line.iloc[15,48:52]
    country4= line.iloc[115,48:52]
    # print all the countries
    print(country1,country2,country3,country4)
    plt.figure()
    
    # to plot and design the line
    plt.plot(country1,label='China',linestyle='dashed')
    plt.plot(country2,label='Denmark',linestyle='dashed')
    plt.plot(country3,label='Argentina',linestyle='dashed')
    plt.plot(country4,label='India',linestyle='dashed')
    # use label to plot the labels
    plt.xlabel('Year')
    # displaying the title
    plt.title('Co2 Emission')
    plt.legend(loc='center left',bbox_to_anchor=(1.40, 0.7))
    plt.show()


 # to define function using def   
def line_plot2(filename):
    # use skiprows if you want to skip headers
    line=pd.read_csv(filename,skiprows=4)
    print(line)
    
    # use iloc to select specific row and column
    country1 = line.iloc[41,35:39]
    country2 = line.iloc[64,35:39]
    country3 = line.iloc[15,35:39]
    country4 = line.iloc[115,35:39]
    
    print(country1,country2,country3,country4)
    plt.figure()
    plt.plot(country1,label='Canada',dashes=[2,1])
    plt.plot(country2,label='Denmark',dashes=[2,1])
    plt.plot(country3,label='Argentina',dashes=[1,4])
    plt.plot(country4,label='India',dashes=[2,5])
    plt.xlabel('Year') 
    
    # displaying the title
    plt.title('Green house')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()

line_plot(r"E:\Co2 emission\Co2 emission1.csv")
line_plot2(r"E:\Green house gas\Green house gas.csv")

# to define function using def
def transpose(filename):
    # use skiprows if you want to skip headers
    csv=pd.read_csv(filename,skiprows=4)
    df_csv = pd.DataFrame(data=csv)
    transposed_csv = df_csv.T  # to transposed data
    # to print transposed data
    print(transposed_csv)    

transpose(r"E:\Forest area\Forest area.csv")
transpose(r"E:\Co2 emission\Co2 emission1.csv")
transpose(r"E:\Population growth\Population growth.csv")
transpose(r"E:\Green house gas\Green house gas.csv")
 
    