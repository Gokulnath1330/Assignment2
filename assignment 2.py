# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:29:59 2022

@author: GOKULNATH
"""

import pandas as pd 
import matplotlib.pyplot as plt


def line_plot(filename):
    # use skiprows if you want to skip headers
    df=pd.read_csv(filename,skiprows=4)
    print(df)
    country1= df.iloc[46,48:52]
    country2= df.iloc[64,48:52]
    country3= df.iloc[15,48:52]
    country4= df.iloc[115,48:52]
    print(country1,country2,country3,country4)
    plt.figure()
    plt.plot(country1,label='China',linestyle='dashed')
    plt.plot(country2,label='Denmark',linestyle='dashed')
    plt.plot(country3,label='Argentina',linestyle='dashed')
    plt.plot(country4,label='India',linestyle='dashed')
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
    country1 = df.iloc[46,47:52]
    country2 = df.iloc[64,47:52]
    country3 = df.iloc[15,47:52]
    country4 = df.iloc[115,47:52]
    print(country1,country2,country3,country4)
    plt.figure()
    plt.plot(country1,label='China',dashes=[2,1])
    plt.plot(country2,label='Denmark',dashes=[2,1])
    plt.plot(country3,label='Argentina',dashes=[1,4])
    plt.plot(country4,label='India',dashes=[2,5])
    plt.xlabel('Year')
    plt.ylabel('% of land area') 
    plt.title('Green house')
    plt.legend(loc='center right',bbox_to_anchor=(1.40, 0.6))
    plt.show()

line_plot(r"E:\Co2 emission\Co2 emission1.csv")
line_plot2(r"E:\Green house gas\Green house gas.csv")


def transpose(filename):
    # use skiprows if you want to skip headers
    csv=pd.read_csv(filename,skiprows=4)
    df_csv = pd.DataFrame(data=csv)
    transposed_csv = df_csv.T
    print(transposed_csv)    

transpose(r"E:\Forest area\Forest area.csv")
transpose(r"E:\Co2 emission\Co2 emission1.csv")
transpose(r"E:\Population growth\Population growth.csv")
transpose(r"E:\Green house gas\Green house gas.csv")

    
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
    bar2.plot(x="Country Name",
              y=["2010","2011","2012","2013","2015"],kind="bar")
    plt.xticks(rotation = 0)
    plt.ylabel('Land area')
    plt.title("Population")
    plt.legend(title='Year',loc='upper center',bbox_to_anchor=(1.10, 0.6))
    plt.show()
Bar_plot(r"E:\Population growth\Population growth.csv")    

def Bar_plot2(filename):
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
    bar2.plot(x="Country Name",
              y=["2010","2011","2012","2013","2015"],kind="bar")
    plt.xticks(rotation = 0)
    plt.ylabel('Land area')
    plt.title("Forest")
    plt.legend(title='Year',loc='upper center',bbox_to_anchor=(1.10, 0.6))
    plt.show()
Bar_plot2(r"E:\Forest area\Forest area.csv")    
    