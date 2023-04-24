reset;
option solver cplex;

#####################################################
# Sets and Parameters
#####################################################
set GAS;
set TANK;

param tankCost {g in GAS, t in TANK}; # Cost per 1000 liters of gas per tank
param tankCap {t in TANK}; # Tank capacity
param gasCap {g in GAS}; # Amount of gas to produce

param k = 8; # There are 8 possible tanks
param M = 200000; # Fun big number

#####################################################
# Decision variables
#####################################################
var intank {g in GAS, t in TANK} >= 0; # The amount of each gas to pump into each tank
var pump {g in GAS, t in TANK} binary; # The decision to pump each gas into each tank

#####################################################
# Objective function
#####################################################
#minimize cost: sum {g in GAS, t in TANK} (0.001 * tankCost[g,t]) * intank[g,t];
minimize cost: sum {g in GAS, t in TANK} pump[g,t] * (0.001 * tankCost[g,t]) * intank[g,t];
#minimize cost: sum {g in GAS, t in TANK} pump[g,t]

#####################################################
# Constraints
#####################################################

s.t. decisions: sum {g in GAS, t in TANK} pump[g,t] <= k; # At most make k decisions (8, one for each tank)
s.t. pumpGas {t in TANK}: sum {g in GAS} pump[g,t] <= 1; # Can at most make one decision per tank
s.t. tankCapacity {t in TANK}: sum {g in GAS} intank[g,t] <= tankCap[t]; # Cannot exceed tank capacity
s.t. gasProduction {g in GAS}: sum {t in TANK} intank[g,t] = gasCap[g]; # Must make this amount of gas
s.t. pumping {g in GAS, t in TANK}: M * pump[g,t] >= intank[g,t]; 


#####################################################
# Data and Solve
#####################################################
data "/Users/anozman/Desktop/ampl/AMPL_workspace/DSA_5113/Homework5/H5Q3.dat";
solve;

#####################################################
# Displays
#####################################################
display cost;
display intank;
display pump;
