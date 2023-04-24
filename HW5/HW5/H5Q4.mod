reset;
option solver cplex;

var prodS integer >= 0; # Production of Space Rays

var ds1 >= 0; # Piecewise production of space rays
var ds2 >= 0;
var ds3 >=0;
var ds4 >=0;

var ys1 binary; # Decision variables to link the piecewise function for space rays
var ys2 binary;
var ys3 binary;


var prodZ integer >= 0; # Production of Zappers

var dz1 >=0; # Piecewise production of zappers
var dz2 >= 0;
var dz3 >=0;

var yz1 binary; # Decision variables to link piecewise function for zappers
var yz2 binary;


#####################################################
# Objective Function
#####################################################
maximize profit: (8-1.5)*ds1 + (8-1.05)*ds2 + (8-0.95)*ds3 + (8-0.75)*ds4 +
				 (5-1.05)*dz1 + (5-0.75)*dz2 + (5-1.5)*dz3;

#####################################################
# Constraints
#####################################################
s.t. total_sr_production: prodS = ds1 + ds2 + ds3 + ds4; # Creating the total production figure for Space Rays
s.t. total_zp_production: prodZ = dz1 + dz2 + dz3; # Creating the total production figure for Zappers

# Linking the Space Ray piecewise function
s.t. pieceSr1a: 125*ys1 <= ds1; # First cut (0-125)
s.t. pieceSr1b: ds1 <= 125;
s.t. pieceSr2a: 100*ys2 <= ds2; # Second cut (125-225)
s.t. pieceSr2b: ds2 <= 100*ds1;
s.t. pieceSr3a: 150*ys3 <= ds3; # Third cut (225-375)
s.t. pieceSr3b: ds3 <= 150*ds2;
s.t. pieceSr4z: ds4 <= 700*ds3; # Fourth cut (375+)

# Linking the Zapper piecewise function
s.t. pieceZp1a: 50*yz1 <= dz1; # First cut (0-50)
s.t. pieceZp1b: dz1 <= 50;
s.t. pieceZp2a: 75*yz2 <= dz2; # Second cut (50-125)
s.t. pieceZp2b: dz2 <= 75*dz1;
s.t. pieceZp3: dz3 <= 700*dz2; # Third cut (125+)

# Prodution and resource constraints
s.t. plastic: 2*prodS + prodZ <= 1000; # Cannot exceed 1000lbs of plastic
s.t. time: ((3/60)*prodS) + ((4/60)*prodZ) <= 40; # 40 hour work week
s.t. total_production: prodS + prodZ <= 700; # Cannot exceed 700 units total
s.t. ratio: prodS - prodZ <= 350; # Cannot produce more than 350 Space rays than Zappers

#####################################################
# Constraints
#####################################################
solve;

display profit;
display prodS;
display prodZ;

