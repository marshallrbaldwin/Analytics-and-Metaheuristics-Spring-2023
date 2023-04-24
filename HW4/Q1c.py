# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:51:41 2023

@author: Marshall Baldwin
"""

output = """
epsilon = 0

:   x     xb       :=
1   0     1e+06
2   0   1060000
3   0   1123600
4   0      .
5   0      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1256492.842
3 dual simplex iterations (1 in phase I)
epsilon = 9628.95

:     x        xb       :=
1        0     1e+06
2        0   1060000
3        0    931021
4        0      .
5   192579      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1321969.684
0 simplex iterations (0 in phase I)
epsilon = 19257.9

:     x        xb       :=
1        0     1e+06
2        0   1060000
3        0    738442
4        0      .
5   385158      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1387446.526
0 simplex iterations (0 in phase I)
epsilon = 28886.8

:     x        xb       :=
1        0     1e+06
2        0   1060000
3        0    545863
4        0      .
5   577737      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1448855.05
1 dual simplex iterations (0 in phase I)
epsilon = 38515.8

:       x         xb       :=
1        0       994921
2        0      1054620
3        0       367893
4     5078.95      .
5   750000         .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1475767.188
0 simplex iterations (0 in phase I)
epsilon = 48144.7

:      x         xb       :=
1        0      946776
2        0     1003580
3        0      313798
4    53223.7      .
5   750000        .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1502679.325
0 simplex iterations (0 in phase I)
epsilon = 57773.7

:     x        xb      :=
1        0   898632
2        0   952549
3        0   259702
4   101368      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1529591.463
0 simplex iterations (0 in phase I)
epsilon = 67402.6

:     x        xb      :=
1        0   850487
2        0   901516
3        0   205607
4   149513      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1556503.601
0 simplex iterations (0 in phase I)
epsilon = 77031.6

:     x        xb      :=
1        0   802342
2        0   850483
3        0   151512
4   197658      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1583415.738
0 simplex iterations (0 in phase I)
epsilon = 86660.5

:     x         xb       :=
1        0   754197
2        0   799449
3        0    97416.2
4   245803       .
5   750000       .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1610327.876
0 simplex iterations (0 in phase I)
epsilon = 96289.5

:     x         xb       :=
1        0   706053
2        0   748416
3        0    43320.7
4   293947       .
5   750000       .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1636193.777
1 dual simplex iterations (0 in phase I)
epsilon = 105918

:      x         xb      :=
1    14248.5   650784
2        0     694105
3        0          0
4   334968        .
5   750000        .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1657853.179
0 simplex iterations (0 in phase I)
epsilon = 115547

:      x         xb      :=
1    85784.3   566871
2        0     626619
3        0          0
4   347345        .
5   750000        .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1679512.58
0 simplex iterations (0 in phase I)
epsilon = 125176

:     x        xb      :=
1   157320   482958
2        0   559132
3        0        0
4   359721      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1701171.982
0 simplex iterations (0 in phase I)
epsilon = 134805

:     x        xb      :=
1   228856   399046
2        0   491645
3        0        0
4   372098      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1722831.383
0 simplex iterations (0 in phase I)
epsilon = 144434

:     x        xb      :=
1   300392   315133
2        0   424159
3        0        0
4   384475      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1744490.785
0 simplex iterations (0 in phase I)
epsilon = 154063

:     x        xb      :=
1   371928   231220
2        0   356672
3        0        0
4   396852      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1766150.187
0 simplex iterations (0 in phase I)
epsilon = 163692

:     x        xb      :=
1   443464   147308
2        0   289185
3        0        0
4   409229      .
5   750000      .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1785752.284
1 dual simplex iterations (0 in phase I)
epsilon = 173321

:     x         xb       :=
1    5e+05    66951.4
2        0   220968
3        0        0
4   433049       .
5   734227       .
;

CPLEX 20.1.0.0: outlev=0
CPLEX 20.1.0.0: optimal solution; objective 1797600
0 simplex iterations (0 in phase I)
epsilon = 182950

:     x             xb           :=
1    5e+05        5.82077e-11
2        0   150000
3        0        0
4    5e+05           .
5   659000           .
;

"""
blocks = output.strip().split("\n\n")

data_dict = {'Risk Threshold' : [],
             'Project 1': [],
             'Project 2': [],
             'Project 3': [],
             'Project 4': [],
             'Project 5': [],
             'Bank Investment 1': [],
             'Bank Investment 2': [],
             'Bank Investment 3': []
             }
for block in blocks:
    lines = block.split("\n")
    for line in lines:
        if line.startswith("epsilon ="):
            elements = line.split(" ")
            data_dict['Risk Threshold'].append(float(elements[-1]))
        
        if line[0].isdigit() and "simplex" not in line:
            digit = int(line[0])
            elements = line.split()
            if digit < 4:
                data_dict[f"Project {digit}"].append(float(elements[1]))
                data_dict[f"Bank Investment {digit}"].append(float(elements[2]))
            else:
                data_dict[f"Project {digit}"].append(float(elements[1]))
   
import numpy as np
for key in data_dict:
    data_dict[key] = np.array(data_dict[key])

from matplotlib import pyplot as plt
fig, ax = plt.subplots(2, sharex = True, figsize = (6,4), dpi = 200)
ax_twin = ax
accumulation = np.zeros(data_dict[key].shape)
linestyles = ['-', '--','-.', ':']
colors = ["black", ]
for idx, key in enumerate(data_dict):
    if "Risk" in key:
        continue
    if "Bank" in key:
        ax[1].plot(data_dict["Risk Threshold"], data_dict[key] / 1_000_000., label = key)
    else:
        ax[0].plot(data_dict["Risk Threshold"], data_dict[key] / 1_000_000., label = key)
    
for axis in ax:
    axis.grid()
    axis.legend(fontsize = 'x-small')
    
fig.suptitle("Investment Amounts as a Function of Risk Score")
fig.text(0, 0.5, 'Investment Amount in Millions [$]', ha='center', va='center', rotation='vertical')
ax[1].set_xlabel("Risk Score")
fig.tight_layout()
