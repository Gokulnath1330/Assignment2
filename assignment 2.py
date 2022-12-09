# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:29:59 2022

@author: GOKULNATH
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def line_plot(filename):
    # use skiprows if you want to skip headers
    df=pd.read_csv(filename,skiprows=4)
    print(df)
    country1 = df.iloc[43,55:61]
    country2 = df.iloc[61,55:61]
    country3= df.iloc[97,55:61]
    country4 = df.iloc[115,55:61]
    print(country1,country2,country3,country4)
    plt.figure()
    plt.plot(country1,label='Switzerland')
    plt.plot(country2,label='Germany')
    plt.plot(country3,label='Greenland')
    plt.plot(country4,label='India')
    # use label to plot the labels
    plt.xlabel('Year')
    plt.ylabel('Co2(kt)') 
    plt.title('Co2 Emission')
    plt.legend(loc='center left',bbox_to_anchor=(1.40, 0.7))
    plt.show()
    
    
def line_plot2(filename):
    # use skiprows if you want to skip headers
    df=pd.read_csv(filename,skiprows=4)
    print(df)
    # use iloc to locate the country location
    country1 = df.iloc[43,54:59]
    country2 = df.iloc[64,54:59]
    country3 = df.iloc[6,54:59]
    country4 = df.iloc[115,54:59]
    print(country1,country2,country3,country4)
    plt.figure()
    plt.plot(country1,label='Switzerland',dashes=[2,1])
    plt.plot(country2,label='Denmark',dashes=[2,1])
    plt.plot(country3,label='South Africa',dashes=[1,4])
    plt.plot(country4,label='India',dashes=[2,5])
    plt.xlabel('Year')
    plt.ylabel('% of land area') 
    plt.title('Forest area (% of land area')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()
line_plot(r"E:\Co2 emission\Co2 emission1.csv")
line_plot2(r"E:\Forest area\Forest area.csv")


def transpose(filename):
    # use skiprows if you want to skip headers
    csv=pd.read_csv(filename,skiprows=4)
    df_csv = pd.DataFrame(data=csv)
    transposed_csv = df_csv.T
    print(transposed_csv)

transpose(r"E:\Forest area\Forest area.csv")
line_plot(r"E:\Co2 emission\Co2 emission1.csv")


  
def Bar_plot(filename):
    # use skiprows if you want to skip headers
    df2=pd.read_csv(filename,skiprows=4)
    df2=df2.drop(["Country Code","Indicator Name","Indicator Code"],axis=1)
    print(df2)
    bar1=df2.fillna(0)
    print(bar1)
    bar2=(bar1.apply(lambda row: row[bar1["Country Name"].
                                     isin(['Switzerland','Denmark','Argentina','India'])]))
    print(bar2)
    plt.figure()
    bar2.plot(x="Country Name",y=["2010","2011","2012","2013","2015"],kind="bar")
    plt.xticks(rotation = 0)
    plt.ylabel('Land area')
    plt.title("Forest")
    plt.legend(loc='upper center',bbox_to_anchor=(1.40, 0.6))
    plt.show()
Bar_plot(r"E:\Population growth\Population growth.csv")    
    