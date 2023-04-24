reset;

option solver cplex;

####################################################
# Decision variables
####################################################
var x1 >= 0, <= 1;
var x2 >= 0, <= 1;
var x3 >= 0, <= 1;
var x4 >= 0, <= 1;

####################################################
# Objective function
####################################################
maximize z: 90*x1 + 55*x2 + 63*x3 + 47*x4;

####################################################
# Constraints
####################################################
s.t. cost: 7*x1 + 2*x2 + 8*x3 + 3*x4 <= 10;
s.t. demand: x3 + x4 <=1;
s.t. odd_choice: -x1 + x3 <= 0;
s.t. even_choice: -x2 + x4 <= 0;

#s.t. constrain_X1: x1 = 1;
#s.t. constrain_X2: x2 = 1;
#s.t. constrain_X3: x3 = 1;
#s.t. constrain_X4: x4 = 1;


solve;
display z;
display x1, x2, x3, x4;