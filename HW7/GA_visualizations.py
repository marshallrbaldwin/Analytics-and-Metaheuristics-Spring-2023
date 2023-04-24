# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 04:25:49 2023

@author: Marshall Baldwin
"""

import pandas as pd
from matplotlib import pyplot as plt
import os

path= "C:\\Users\\nimzo\\Documents\\Analytics and Metaheuristics\\Homeworks\\HW7\\run_logs"
run_csvs = os.listdir(path)

def scrape_csv_filename(f):
    chunks = f.split("_")
    populationSize = int(chunks[2][3:])
    Generations = int(chunks[3][3:])
    crossOverRate = float(chunks[4][3:])
    mutationRate = float(chunks[5][3:])
    mutationProportion = float(chunks[6][5:])
    eliteSolutions = int(chunks[7][3:])
    seed = int(chunks[8][4:-4])
    
    return (populationSize, Generations, crossOverRate, mutationRate,
            mutationProportion, eliteSolutions, seed)


for f in run_csvs:
    pop, gen, COR, mRt, mProp, elt, seed = scrape_csv_filename(f)
    data = pd.read_csv(f"{path}\\{f}")
    wgt = data['BestWeight'].values[-1]
    val = data['BestValue'].values[-1]
    ct = data['BestItem'].values[-1]
    
    print(pop, gen, COR, mRt, mProp, elt, wgt, val, ct, sep=",")

filename=f"{path}\\GA_knapsack_pop200_gen500_COR0.8_mRt0.4_mProp0.02_elt10_seed51132023.csv"
data = pd.read_csv(filename)

#sraping info from name
chunks = f.split("_")
populationSize = int(chunks[2][3:])
Generations = int(chunks[3][3:])
crossOverRate = float(chunks[4][3:])
mutationRate = float(chunks[5][3:])
mutationProportion = float(chunks[6][5:])
eliteSolutions = int(chunks[7][3:])
seed = int(chunks[8][4:-4])

labels = ['Generation', 'MaxFitness', 'MinFitness', 'MeanFitness', 'StdvFitness',
       'BestItem', 'BestValue', 'BestWeight']


fig, ax = plt.subplots(3,1, figsize = (6, 6), dpi = 300)

ax[0].plot(data['Generation'].values, data['BestItem'].values, color = 'black',
           linewidth = 2)
ax[1].plot(data['Generation'].values, data['BestValue'].values,color = 'black',
           linewidth = 2)
ax[2].plot(data['Generation'].values, data['BestWeight'].values,color = 'black',
           linewidth = 2)

ylabs = ["Number of Items","Total Value","Weight"]
for i in range(3):
    ax[i].grid()
    ax[i].set_ylabel(ylabs[i], fontsize = 13)
ax[2].set_xlabel("Generations")

param_info1 = f"Parameters: popSize={populationSize}, crossoverRate={crossOverRate}, "

param_info2 = f"mutationRate={mutationRate}, \nmutationProportion={mutationProportion}, "
param_info3 = f"eliteSolutions={eliteSolutions}, seed={seed}"
param_info = param_info1+param_info2+param_info3
ax[0].set_title(param_info, fontsize = 8)
fig.suptitle("Best Solution Characteristics for Each Generation", fontsize = 15)
plt.tight_layout()
plt.show()


#general population information
fig, ax = plt.subplots(1, figsize = (6, 3), dpi = 200)

ax.plot(data['Generation'].values, data['MaxFitness'].values, color = 'blue')
ax.plot(data['Generation'].values, data['MinFitness'].values, color = 'red')
ax.plot(data['Generation'].values, data['StdvFitness'].values, color = 'black')


ax.set_title("Population's Best/Worst (Blue/Red) Fitness and Mean (Black) of Fitnesses")
ax.grid()
plt.tight_layout()


