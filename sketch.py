import DNA
import Population

## Setup
target = 'To be or not to be.'
popMax = 200
mutationRate = 0.01

population = Population.Population(target, mutationRate, popMax)

while(not population.isFinished()):
    ## Generate new mating pool
    population.naturalSelection()
    ## Create next Generation
    population.generate()
    ## Calculate fitness
    population.calcFitness()
    ## evaluate
    population.evaluate()

    displayInfo()


def displayInfo():
    answer = population.getBest()
    print('*********************************************')
    print(answer)
    print('total generations: ', population.getGenerations())
    print('average fitness: ', population.getAvgFitness())
    print('total population: ', popMax)
    print('mutation rate: ', mutationRate)
    print('\n')
    print('All Phrases:\n ', population.allPhrases())
    print('*********************************************')
    
    
