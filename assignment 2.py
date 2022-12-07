# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:29:59 2022

@author: GOKULNATH
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
def line_plot(filename):
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
    plt.xlabel('Year')
    plt.ylabel('Co2(kt)') 
    plt.title('Co2 Emission')
    plt.legend(loc='center left',bbox_to_anchor=(1.40, 0.7))
    plt.show()

    