#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize

import os
import requests


########################## FITTING FUNCTIONS ####################################
def func_expo(x, a, b):
    return a * np.exp(b * x)

def func_logistic(x, x0, k, V):
    return V/(1+np.exp(k*(x-x0)))

def func_geometric(x,a,n):
    return a*x**n


#################################################################################
def prepare_data(data, country):
    df = data[ data['countriesAndTerritories']==country]
    df['n'] = np.linspace(len(df),1, len(df)).astype('int')
    
    sum_cases = []

    for n in range(1,len(df)+1):
        sum_cases.append(sum(df[ df['n'] <n+2]['cases']))
    sum_cases.reverse()
    df['all'] = sum_cases
    df.drop(df.tail(1).index,inplace=True)
    
    return df


#################################################################################


def plot_all(country, max_x = 100, max_y = 5500):
    
    parameters_logistic = scipy.optimize.curve_fit(func_logistic, country['n'],  country['all'])[0]
    parameters_expo = scipy.optimize.curve_fit(func_expo,  country['n'],  country['all'])[0]
    
    print("parameters: logistic {:}".format(parameters_logistic) )
    print("parameters: expo {:}".format(parameters_expo) )        
     
    x = np.linspace(0,max_x, max_x+1)
    
    a = parameters_expo[0]
    b = parameters_expo[1]
    y_expo = func_expo(x, a, b)

    x0 = parameters_logistic[0]
    k = parameters_logistic[1]
    V = parameters_logistic[2]
    y_logistic = func_logistic(x,x0,k,V)

    fig, axs = plt.subplots(ncols=2, figsize = (15,4))

    axs[0].scatter(country['n'], country['all'], label="data points", color = "purple")
    axs[0].plot(x, y_expo, label="exponential fit", color = 'gray')

    axs[1].scatter(country['n'], country['all'], label="data points", color = "purple")
    axs[1].plot(x, y_logistic, label="logistic function fit", color = 'gray')
    axs[1].axhline(y=V, color='black', linestyle = '--')

    for ax in axs:
        ax.set_xlabel('day')
        ax.set_ylabel('number of infected')
        ax.set_ylim(0,max_y) 
        ax.legend()
        ax.grid(color = 'gray', alpha = 0.4)

    plt.show()



def plot_delta(country):
    pass


