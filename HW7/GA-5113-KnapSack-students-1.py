#basic genetic algorithm Python code provided as base code for the DSA/ISE 5113 course
#author: Charles Nicholson
#date: 4/5/2019

#NOTE: You will need to change various parts of this code.  However, please 
#keep the majority of the code intact (e.g., you may revise existing 
#logic/functions and add new logic/functions, but don't completely rewrite 
#the entire base code!)  
#However, I would like all students to have the same problem instance, 
#therefore please do not change anything relating to:
#   random number generation
#   number of items (should be 150)
#   random problem instance
#   weight limit of the knapsack

#------------------------------------------------------------------------------

#Student name: Marshall Baldwin
#Date: 4-23-2023


#need some python libraries
import copy
import math
from random import Random
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
    #value.append(round(myPRNG.expovariate(1/500)+1,1))
    value.append(round(myPRNG.triangular(150,2000,500),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(8,300,95),1))
    
#define max weight for the knapsack
maxWeight = 2500

#change anything you like below this line, but keep the gist of the program ------------------------------------

#change value and weights to numpy arrays for ease of use
value = np.array(value)
weights = np.array(weights)

#length of a solution chromosome
sol_len = value.size

#make np randomness deterministic
np.random.seed(seed)

#monitor the number of solutions evaluated
solutionsChecked = 0

populationSize = 200 #size of GA population; must be even number
Generations = 500   #number of GA generations

crossOverRate = 0.8
mutationRate = 0.4
mutationProportion = 0.02
eliteSolutions = 10 

def createChromosome(zero_bias = .8):   
    #create a solution to the knapsack problem in binary format
    
    #I'm choosing to bias towards an emptier knapsack i.e. 85% 0s
    x = np.random.choice(2,size = sol_len, p = [zero_bias,1.-zero_bias])
    
    return x    


#function to evaluate a solution x and return a fitness score
potential_value = np.sum(value)
def itemsSelected(x): return float(np.sum(x))
def calcWeight(x): return np.dot(x,weights)
def getValue(x): return np.dot(x,value)

def evaluate(x):

    #keep track of solutions checked lol
    global solutionsChecked
    solutionsChecked += 1
    
    totalValue =  getValue(x) #value of items in solution's knapsack
    totalWeight = calcWeight(x)    #weight of items in solution's knapsack
    totalItems = itemsSelected(x)  #number of items in knapsack
    
    if totalWeight > maxWeight:
        return 0.00000001
    
    #metrics within [0,1] describing value compared to maximum possible
    weightEfficiency = totalWeight / float(maxWeight)
    valueEfficiency = totalValue / potential_value
    spaceEfficiency = totalItems / float(sol_len)
    
    #return (weightEfficiency + valueEfficiency + spaceEfficiency) / 3.
    return spaceEfficiency * (valueEfficiency / (weightEfficiency+.0001))
    
    
def initializePopulation():
    
    #create population of and score each chromosome
    population = np.empty(shape = (populationSize, sol_len))
    populationFitness = np.empty(shape = populationSize)
    for i in range(populationSize):
        population[i] = createChromosome()
        populationFitness[i] = evaluate(population[i])
    
    #sort members in order of descending fitness
    sorted_fitness_indices = np.argsort(populationFitness)[::-1]
    population = population[sorted_fitness_indices]
    populationFitness = populationFitness[sorted_fitness_indices]
    
    return population, populationFitness 

def crossover(x1,x2, COR = crossOverRate):
    
    #chance to not splice genes
    cross_threshold = myPRNG.random()
    if cross_threshold > COR:
        return x1, x2
    
    #create new arrays for offspring
    offspring1 = np.empty(x1.size)
    offspring2 = np.empty(x1.size)
    
    #randomly determine splice point drawing from a Gaussian centered around
    #the middle of the chromosome
    lower_bound = 1
    upper_bound = x1.size - 1
    mu = (lower_bound + upper_bound) / 2.  # middle of the range
    sigma = (upper_bound - lower_bound) / 8.  #assuming lower and upper bounds lie at +/- 4 sigma
    sample = np.random.normal(mu, sigma) #use numpy to do the gaussian sample
    splice_idx = np.clip(round(sample), lower_bound, upper_bound) 
    
    #do the splice
    offspring1[:splice_idx] = x1[:splice_idx]
    offspring1[splice_idx:] = x2[splice_idx:]
    offspring2[:splice_idx] = x2[:splice_idx]
    offspring2[splice_idx:] = x1[splice_idx:]
    
    return offspring1, offspring2  #two offspring are returned 


#performs tournament selection; k chromosomes are selected (with repeats allowed) and the best advances to the mating pool
#function returns the mating pool with size equal to the initial population
def tournamentSelection(pop,k):
    
    #randomly select k chromosomes; the best joins the mating pool
    matingPool = []
    
    while len(matingPool)<populationSize:
        
        ids = [myPRNG.randint(0,populationSize-1) for i in range(k)]
        competingIndividuals = [pop[i][1] for i in ids]
        bestID=ids[competingIndividuals.index(max(competingIndividuals))]
        matingPool.append(pop[bestID][0])

    return matingPool


def rouletteWheel(pop, fitnesses):
    
    #probability of selection for an individual is equal to the proportion
    #of total fitness its score contributes to the population
    selection_probs = fitnesses / fitnesses.sum()
    
    #use numpy choice to select with replacement from population (bagging)
    selection_indices = np.random.choice(populationSize, size = populationSize,
                                         replace=True, p=selection_probs)
    matingPool = pop[selection_indices]
      
    return matingPool
    
    
#function to mutate solutions
def mutate(x, mutRate = mutationRate, mutProp = mutationProportion):
    
    #decide whether or not to mutate
    mutation_threshold = myPRNG.random()
    if mutation_threshold > mutRate:
        return x
    
    #flip random indices
    flip_amount = round(sol_len * mutProp)
    flipped_indices = np.random.choice(sol_len, size = flip_amount, replace = True)
    for idx in flipped_indices:
        x[idx] = (x[idx] + 1) % 2
    
    return x 
            
    
   
def breeding(matingPool):
    
    #create arrays for children and their respective fitness
    children = np.empty(shape = (populationSize, sol_len))
    childrenFitness = np.empty(populationSize)
    
    #the parents will be the first two individuals, then next two, and so on
    for i in range(0,populationSize-1,2):
        child1,child2=crossover(matingPool[i],matingPool[i+1])
        
        child1=mutate(child1)
        child2=mutate(child2)
        
        children[i] = child1
        children[i+1] = child2
        
        childrenFitness[i] = evaluate(child1)
        childrenFitness[i+1] = evaluate(child2)
    
    #sort children in order of descending fitness
    sorted_fitness_indices = np.argsort(childrenFitness)[::-1]
    children = children[sorted_fitness_indices]
    childrenFitness = childrenFitness[sorted_fitness_indices]
        
    return children, childrenFitness


#insertion step
def insert(pop, popFit, kids, kidFit, elite_retention = eliteSolutions):
    
    #insert top 10 from prev gen
    kids[-eliteSolutions:] = pop[:eliteSolutions]
    kidFit[-eliteSolutions:] = popFit[:eliteSolutions]
    
    #sort arrays
    sorted_fitness_indices = np.argsort(kidFit)[::-1]
    kids=kids[sorted_fitness_indices]
    kidFit=kidFit[sorted_fitness_indices]
    
    return kids, kidFit
    
    
    
#perform a simple summary on the population: returns the best chromosome fitness, the average population fitness, and the variance of the population fitness
def summaryFitness(popFit):
    return np.max(popFit), np.mean(popFit), np.min(popFit), np.std(popFit)
def bestSolutionInfo(pop):
    return itemsSelected(pop[0]), getValue(pop[0]), calcWeight(pop[0])

#the best solution should always be the first element... 
def bestSolutionInPopulation(pop):
    print ("Best solution: ", pop[0])
    print ("Items selected: ", itemsSelected(pop[0]))
    print ("Value: ", getValue(pop[0]))
    print ("Weight: ", calcWeight(pop[0]))

    
    
def main():
    
    #make np randomness deterministic
    np.random.seed(1243267)
    
    #Create initial population and evaluate fitness
    population, fitnesses = initializePopulation()
    maxVal, meanVal, minVal, stdVal=summaryFitness(fitnesses)
    bestItems,bestVal,bestWgt = bestSolutionInfo(population)
    
    filename = f'run_logs/GA_knapsack_pop{populationSize}_gen{Generations}_COR{crossOverRate}_mRt{mutationRate}_mProp{mutationProportion}_elt{eliteSolutions}_seed{seed}.csv'
    f = open(filename, 'w')
    f.write('Generation,MaxFitness,MinFitness,MeanFitness,StdvFitness,BestItem,BestValue,BestWeight,SolutionsChecked\n')
    f.write(f"0,{maxVal},{minVal},{meanVal},{stdVal},{bestItems},{bestVal},{bestWgt},{solutionsChecked}\n")
    
    #step through generations to improve solution
    for j in range(Generations):
        
        #select next generation
        mates=rouletteWheel(population, fitnesses)
        offspring, child_fitness = breeding(mates)
        population, fitnesses = insert(population,fitnesses,
                                       offspring,child_fitness)
    
        #get new generation's info
        maxVal, meanVal, minVal, stdVal=summaryFitness(fitnesses)
        bestItems,bestVal,bestWgt = bestSolutionInfo(population)
        
        f.write(f"{j+1},{maxVal},{minVal},{meanVal},{stdVal},{bestItems},{bestVal},{bestWgt},{solutionsChecked}\n")
        
    f.close()
    
    bestSolutionInPopulation(population)
    

if __name__ == "__main__":
    main()    
    


