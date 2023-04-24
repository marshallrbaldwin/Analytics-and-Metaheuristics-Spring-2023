#basic hill climbing search provided as base code for the DSA/ISE 5113 course
#author: Charles Nicholson
#date: 4/5/2019

#NOTE: You will need to change various parts of this code.  However, please keep the majority of the code intact (e.g., you may revise existing logic/functions and add new logic/functions, but don't completely rewrite the entire base code!)  
#However, I would like all students to have the same problem instance, therefore please do not change anything relating to:
#   random number generation
#   number of items (should be 150)
#   random problem instance
#   weight limit of the knapsack

#------------------------------------------------------------------------------

#Student name:
#Date: 


#need some python libraries
import copy
from random import Random   #need this for the random number generation -- do not change
import numpy as np


#to setup a random number generator, we will specify a "seed" value
#need this for the random number generation -- do not change
seed = 51132023
myPRNG = Random(seed)

#to get a random number between 0 and 1, use this:             myPRNG.random()
#to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
#to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

#number of elements in a solution
n = 150

#create an "instance" for the knapsack problem
value = []
for i in range(0,n):
    value.append(round(myPRNG.triangular(5,1000,200),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(10,200,60),1))
#define max weight for the knapsack
maxWeight = 2500

#change anything you like below this line ------------------------------------

#monitor the number of solutions evaluated
solutionsChecked = 0

# This method is used to define the infeasibility problem
# This method makes the total value of the infeasible problem 0 and maxes the weight, nullifying its favorability in the solution set
# Marshall tell me if I'm out of pocket for this, but it seemed like a good way to discount the scenario
def solve_infease_by_nullValue():
    return 0, maxWeight

# The goal of this method is very similar to the previous solution
# If the value is over the weight limit, gives the weight and value a flag value, thus indicating their loss
def solve_infease_by_flagValue():
    return -999, -999


#function to evaluate a solution x
def evaluate(x):
          
    a=np.array(x)
    b=np.array(value)
    c=np.array(weights)
    
    totalValue = np.dot(a,b)     #compute the value of the knapsack selection
    totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection
    
    if totalWeight > maxWeight:
        
        # Give the inveasibility solution a flag value if found to be over the weight limit of the knapsack
        totalValue, totalWeight = solve_infease_by_flagValue()
      
    return [totalValue, totalWeight]   #returns a list of both total value and total weight

def evaluate_efficiency(x):
    
    a=np.array(x)
    b=np.array(value)
    c=np.array(weights)
    
    totalValue = np.dot(a,b)     #compute the value of the knapsack selection
    totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection
    efficiency = totalValue/totalWeight
    
#here is a simple function to create a neighborhood
#1-flip neighborhood of solution x         
def neighborhood(x):
        
    nbrhood = []     
    
    for i in range(0,n):
        nbrhood.append(x[:])
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
      
    return nbrhood

# Generates a neighborhood very similar to the 1-flip neighborhood solution
# Creates a neighborhood by changinging the ith element to the i+jth value
def neighborhood_by_j_shift(x,j,n = 150):
    nbrhood = []
    for i in range(0,n):
        nbrhood.append(x[:])
        if i+j < n:
            nbrhood[i][i] = nbrhood[i][i+j]
        else: # Loops to the front of the array
            nbrhood[i][i] = nbrhood[i][i+j-n]
    return nbrhood

# Generates a neighborhood by generating n solutions, each with j flips within it
# While the number of flips are the same throughout the experiment, the elements flipped are randomized          
def neighborhood_by_j_flips(x,j,n = 150):
    nbrhood = []
    for i in range(0,n):
        nbrhood.append(x[:])
        for k in range(0,j):
            item = myPRNG.randint(0,n-1) # Generate a random integer
            if nbrhood[i][item] == 0:
                nbrhood[i][item] = 1
            else:
                nbrhood[i][item] = 0
    return nbrhood



#create the initial solution
def initial_solution():
    x = []   #i recommend creating the solution as a list
    
    for i in range(n):
    
        x.append(i)  #this is certainly wrong!
        
    return x

# This initial solution strategy generates the solution by randomly selecting items and adding their weights, then returning when weight is met or exceeded by the first item to do so
def init_solution_by_random():
    x = [] # List of items
    total_weight = 0 # Sumation of weight of the items in x
    while total_weight <= maxWeight:
        item = myPRNG.randint(0,n-1) # Generate a random integer
        if item not in x: # Does not allow duplicates of an item to be stored
            if total_weight + weights[item] <= maxWeight: # Checks to see if the weight limit is exceeded
                x.append(item)
                total_weight += weights[item]
            else: # If weight limit is exceeded, exit protocol initiated
                soln_list = []
                #print(np.sort(x))
                for i in range(0,len(value)): # Converts the list of objects into 1,0 if object is/not included in solution
                    if i in x:
                        soln_list.append(1)
                    else:
                        soln_list.append(0)
                return soln_list
        #print(x)

# This initial solution strategy generates a solution by selecting the items by their max value and adding their weights until the weight limit is met or exceeded
# NOTE: This will yield the same initial starting solution for constant dataset
def init_solution_by_maxValue():
    x = [] # List of items 
    total_weight = 0 # Summation of weight of items in x
    temp_values = np.copy(value) # Temporary value array duplicate
    while total_weight <= maxWeight:
        item = np.argmax(temp_values) # Finds the item with the highest value in the values dataset 
        if total_weight + weights[item] <= maxWeight: # If adding the item to the knapsack does not exceed the weight limit, do the following tasks
            x.append(item) # Add item to knapsack
            total_weight += weights[item] # Combine the summed weights
            temp_values = np.delete(temp_values, item) # Delete the item from the values array to prevent duplicates
        else: # If adding the item will overload the knapsack, return the list of items
            soln_list = []
            for i in range(0,len(value)): # Converts the list of objects into 1,0 if object is/not included in solution
                if i in x:
                    soln_list.append(1)
                else:
                    soln_list.append(0)
            return soln_list
        #print(x)

def init_solution_empty():

#Question 4 Solution
def HCRR(k, vals, wgts):
    """
    Algorithm for hill climbing with random restarts
    k = number of random restarts
    vals = values of items in knapsack
    wgts = weights of items in knapsack
    """
    #for k rounds, initializes randomly and then finds local maximum
    
    total_solns_checked = 0
    nbrhood_size = 150
    nbrhood_j = len(vals) // 8 #number of flips  
    
    solutions = [] #stores best solution from each round
    solution_scores = [] #stores score for each of those solutions
    solution_weights = [] #use these in the case of a tiebreaker for best solution
    
    for _ in range(k):
        x_curr = init_solution_by_random() #get random first guess
        best_soln = x_curr #our first guess is our best guess so far
        best_soln_eval = evaluate(best_soln) #evaluate quality of first guess
        total_solns_checked += 1
        
        #set up local search from this solution
        not_done = True
        safety_counter = 0 #makes sure we don't get stuck in an infinite loop
        while not_done and safety_counter < 1_000_000_000:
            
            #get alternate solutions from neighborhood
            #NOTE: This neighborhood definition is a hyperparameter!
            nbrhood = neighborhood_by_j_flips(x_curr, nbrhood_j, nbrhood_size) 
            
            #check each solution in the neighborhood
            #NOTE: I'll use first improvement rather than best improvement
            for soln in nbrhood:
                
                soln_eval = evaluate(soln) #returns [value, weight] of soln
                total_solns_checked += 1
                
                #is the solution better than our current best?
                if soln_eval[0] > best_soln_eval[0]:
                    best_soln = soln[:] #if so, make it our new solution
                    best_soln_eval = soln_eval[:] #update best evaluation
            
            #if our current solution is still the best after looking through
            #the whole neighborhood, then we end the search
            if x_curr == best_soln:
                not_done = False
                solutions.append(best_soln)
                solution_scores.append(best_soln_eval[0])
                solution_weights.append(best_soln_eval[1])
            #otherwise replace current solution with better one
            #before searching its local space
            else:
                x_curr = best_soln
                #no need to update best soln... it's already assigned above
            
            safety_counter += 1
        
        safety_counter = 0
        
    #now that we've done our k searches, find the best solution
    top_score = -1000. #initial guess lower than even an infeasible soln
    top_solutions = [] #list of best solutions; hopefully only 1!
    top_solution_indices = [] #store the locations of top solutions
    for idx, score in enumerate(solution_scores):
        if score >= top_score:
            top_score = score #update top score
            top_solutions = [] #empty the list
            top_solutions.append(solutions[idx]) #append solution
            top_solution_indices.append(idx) #append solution index
            
        #tiebreaker case
        elif score == top_score:
            top_solutions.append(solutions[idx])
            top_solution_indices.append(idx)
            
    #Find index of solution with least weight
    top_idcs = np.array(top_solution_indices)
    min_wgt_idx = np.array(solution_weights)[top_idcs].argmin()
    soln_idx = top_solution_indices[min_wgt_idx]
    return {"Best Solution"     : solutions[soln_idx],
            "Value"             : solution_scores[soln_idx],
            "Weight"            : solution_weights[soln_idx],
            "Items"             : sum(solutions[soln_idx]),
            "Solutions Checked" : total_solns_checked,
            "k"                 : k
        }

def display_HCRR_results(result_dict):
    print(f"\nFor a hill climbing algorithm with {result_dict['k']} random restarts we get:")
    print(f"Final number of solutions checked: {result_dict['Solutions Checked']}")
    print(f"Best value found: {result_dict['Value']}")
    print(f"Weight is: {result_dict['Weight']}")
    print(f"Total number of items selected: {result_dict['Items']}")
    print(f"Best solution: {result_dict['Best Solution']}\n")

#run the algorithm for different k's
'''
HCRR_k20_soln = HCRR(10, value, weights)
display_HCRR_results(HCRR_k20_soln)
HCRR_k25_soln = HCRR(25, value, weights)
display_HCRR_results(HCRR_k25_soln)
HCRR_k50_soln = HCRR(50, value, weights)
display_HCRR_results(HCRR_k50_soln)
'''

#Question 5 Solution
def HCRW(p, rng, vals, wgts):
    """
    Algorithm for hill climbing with random walk
    p = probability of hill climbing at a given step; float in [0,1]
    rng = Random object instance for random number generation
    vals = values of items in knapsack
    wgts = weights of items in knapsack
    """
    total_solns_checked = 0
    nbrhood_size = 150
    nbrhood_j = len(vals) // 8 #number of flips
    
    x_curr = init_solution_by_random() #get random first guess
    best_soln = x_curr #our first guess is our best guess so far
    best_soln_eval = evaluate(best_soln) #evaluate quality of first guess
    total_solns_checked += 1
    
    not_done = True
    safety_counter = 0 #makes sure we don't get stuck in an infinite loop
    while not_done and safety_counter < 1_000_000_000:  
        
        #generate neighborhood
        nbrhood = neighborhood_by_j_flips(x_curr, nbrhood_j, nbrhood_size)
        
        #use rng to see if random walk is selected
        decision = rng.randint(0, 1_000_000) / 1000000.0
        #random walk component
        if decision > p:
            rand_stumble = rng.randrange(len(nbrhood)) #random index from nbrhood
            x_curr = nbrhood[rand_stumble]
            best_soln_eval = evaluate(best_soln)
            total_solns_checked += 1
            continue
        
        #otherwise search neighborhood with a hill climbing algorithm
        for soln in nbrhood:
            soln_eval = evaluate(soln) #returns [value, weight] of soln
            total_solns_checked += 1
            
            #is the solution better than our current best?
            
            if soln_eval[0] > best_soln_eval[0]:
                best_soln = soln[:] #if so, make it our new solution
                best_soln_eval = soln_eval[:] #update best evaluation
        
        #after searching the whole neighborhood, if the current solution is
        #still the best, then stop the loop
        if x_curr == best_soln:
            break
        
        #update current solution before exploring its neighborhood
        x_curr = best_soln
        safety_counter += 1
    
    return {"Best Solution"     : x_curr,
            "Value"             : best_soln_eval[0],
            "Weight"            : best_soln_eval[1],
            "Items"             : sum(x_curr),
            "Solutions Checked" : total_solns_checked,
            "p"                 : p
        }

def display_HCRW_results(result_dict):
    print(f"\nFor a hill climbing algorithm with probability {1.0 - result_dict['p']} of a random walk, we get:")
    print(f"Final number of solutions checked: {result_dict['Solutions Checked']}")
    print(f"Best value found: {result_dict['Value']}")
    print(f"Weight is: {result_dict['Weight']}")
    print(f"Total number of items selected: {result_dict['Items']}")
    print(f"Best solution: {result_dict['Best Solution']}\n")

#run the algorithm for different p's
#HCRW_p50_soln = HCRW(.8, myPRNG, value, weights)
#display_HCRW_results(HCRW_p50_soln)
#HCRW_p50_soln = HCRW(.95, myPRNG, value, weights)
#display_HCRW_results(HCRW_p50_soln)

#Question 6 Solution
def get_weighted_probs(score_improvements):
    """
    Returns list of probabilities for each score improvement
    based on their proportion of contribution to total score improvement
    """
    probs = []
    total_improvement = sum(score_improvements)  
    for x in score_improvements:
        probs.append(float(x) / total_improvement)
    
    return probs

def SHC(vals, wgts, is_weighted = True):
    """
    Algorithm for stochastic hill climbing
    vals = values of items in knapsack
    wgts = weights of items in knapsack
    is_weighted = boolean value denoting whether to weight probabilities
                  of picking solutions based on their magnitude of improvement 
                  or to simply use a uniform distribution
    """
    total_solns_checked = 0
    nbrhood_size = 150
    nbrhood_j = len(vals) // 8 #number of flips
    
    x_curr = init_solution_by_random() #get random first guess
    x_curr_eval = evaluate(x_curr) #evaluate quality of first guess
    total_solns_checked += 1
    
    #enter the hill climbing algorithm
    not_done = True
    safety_counter = 0 #makes sure we don't get stuck in an infinite loop
    while not_done and safety_counter < 1_000_000_000:  
        
        #get neighborhood for current solution
        nbrhood = neighborhood_by_j_flips(x_curr, nbrhood_j, nbrhood_size)
        
        #search neighborhood for a better solution
        improving_solutions = []
        improving_evals = []
        for soln in nbrhood:
            #evaluate the solution
            soln_eval = evaluate(soln) #returns [value, weight] of soln
            total_solns_checked += 1
            
            #is the solution better than our current best?
            if soln_eval[0] > x_curr_eval[0]:
                #if so, add it to list of improving solutions
                improving_solutions.append(soln[:])
                improving_evals.append(soln_eval[:]) #save evaluation data too
        
        #after searching the whole neighborhood, if the current solution is
        #still the best, then stop the loop
        if len(improving_solutions) == 0:
            break
        #if there's only one better solution, follow it
        if len(improving_solutions) == 1:
            x_curr = improving_solutions[0]
            x_curr_eval = improving_evals[0]
        else:
            if is_weighted:
                score_improvements = [ev[0] - x_curr_eval[0] for ev in improving_evals]
                prob_dist = get_weighted_probs(score_improvements)
                chosen_idx = np.random.choice(len(score_improvements), p = prob_dist)
                x_curr = improving_solutions[chosen_idx]
                x_curr_eval = improving_evals[chosen_idx]
            else:
                #note that choice does a uniform distribution by default
                chosen_idx = np.random.choice(len(score_improvements))
                x_curr = improving_solutions[chosen_idx]
                x_curr_eval = improving_evals[chosen_idx]
                
        safety_counter += 1
    
    return {"Best Solution"     : x_curr,
            "Value"             : x_curr_eval[0],
            "Weight"            : x_curr_eval[1],
            "Items"             : sum(x_curr),
            "Solutions Checked" : total_solns_checked
        }

def display_SHC_results(result_dict, is_weighted = True):
    if is_weighted:
        print("\nFor a stochastic hill climbing algorithm with a weighted choice distribution, we get:")
    else:
        print("\nFor a stochastic hill climbing algorithm with a uniform choice distribution, we get:")
    print(f"Final number of solutions checked: {result_dict['Solutions Checked']}")
    print(f"Best value found: {result_dict['Value']}")
    print(f"Weight is: {result_dict['Weight']}")
    print(f"Total number of items selected: {result_dict['Items']}")
    print(f"Best solution: {result_dict['Best Solution']}\n")
 
#run the algorithm for weighted and unweighted versions
SHC_unWgt_soln = SHC(value, weights, is_weighted = False)
display_SHC_results(SHC_unWgt_soln, is_weighted = False)
SHC_Wgt_soln = SHC(value, weights)
display_SHC_results(SHC_Wgt_soln)

#%%
#varaible to record the number of solutions evaluated
solutionsChecked = 0

#x_curr = initial_solution()  #x_curr will hold the current solution 
'''
print("Initial solution solver: Random Solution")
x_curr = init_solution_by_random()
'''
print("Initial solution solver: Max Value")
x_curr = init_solution_by_maxValue()

print(x_curr)
x_best = x_curr[:]           #x_best will hold the best solution 
f_curr = evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
f_best = f_curr[:]

#j = myPRNG.randint(1,n-1) # Needs to create a j shift that is at least 1 and less than n
j = 36
print("Neighborhood strategy: 1-flip")
#print("Neighborhood stragegy: j-shift, j=" + str(j))
#print("Neighborhood stragegy: j-flips, j=" + str(j))

#begin local search overall logic ----------------
done = 0

#
while done == 0:
            
    Neighborhood = neighborhood(x_curr)   #create a list of all neighbors in the neighborhood of x_curr
    #Neighborhood = neighborhood_by_j_shift(x_curr, j) # j shift neighborhood
    #Neighborhood = neighborhood_by_j_flips(x_curr, j) # j shift neighborhood
    
    for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1
        if evaluate(s)[0] > f_best[0]:   
            x_best = s[:]                 #find the best member and keep track of that solution
            f_best = evaluate(s)[:]       #and store its evaluation
            break                         # FIRST IMPROVEMENT
    
    if f_best == f_curr:                  #if there were no improving solutions in the neighborhood
        done = 1
    else:
        
        x_curr = x_best[:]         #else: move to the neighbor solution and continue
        f_curr = f_best[:]         #evalute the current solution
        
        print ("\nTotal number of solutions checked: ", solutionsChecked)
        print ("Best value found so far: ", f_best)        
    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
