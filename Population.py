import DNA
import random

class Population:
    
    def __init__(self, target, mutationRate, num):
        self.population = []
        self.matingPool = []
        self.generations = 0
        self.finished = False
        self.target = target
        self.mutationRate = mutationRate
        self.perfectScore = 1

        self.best = ''

        for i in range(num):
            self.population.append(DNA.DNA(len(self.target)))


    def calcFitness(self):
        for i in range(len(self.population)):
            self.population[i].calcFitness(self.target)

        ###generate mating pool
 
    def naturalSelection(self):
        self.matingPool = []

        maxFitness = 0
        for i in range(len(self.population)):
             if(self.population[i].fitness > maxFitness):
                 maxFitness = self.population[i].fitness
        #print(maxFitness)

        if(maxFitness != 0.0):
            for i in range(len(self.population)):
                fitness = self.population[i].fitness/(maxFitness)
                n = round(fitness*100)
            
                for j in range(n):
                    self.matingPool.append(self.population[i])

        else:
            for i in range(len(self.population)):
                self.matingPool.append(self.population[i])
            


    ### new generation

    def generate(self):
        for i in range(len(self.population)):
            a = random.randint(0, len(self.matingPool)-1)
            b = random.randint(0, len(self.matingPool)-1)
            #print(a)

            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]

            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            self.population[i] = child

        self.generations = self.generations + 1

    def getBest(self):
        return self.best

    #### evaluate most fit member of the population

    def evaluate(self):
        worldrecord = 0.0
        index = 0
        for i in range(len(self.population)):
            if(self.population[i].fitness > worldrecord):
                index = i
                worldrecord = self.population[i].fitness

        self.best = self.population[index].getPhrase()
        if(worldrecord == self.perfectScore):
            self.finished = True

    def isFinished(self):
        return self.finished

    def getGenerations(self):
        return self.generations

    def getAvgFitness(self):
        total = 0
        for i in range(len(self.population)):
            total = total + self.population[i].fitness

        return total/len(self.population)

    def allPhrases(self):
        everything = ''
        displayLimit = min(len(self.population), 50)

        for i in range(displayLimit):
            everything = everything + self.population[i].getPhrase() + ' | '

        return everything

    














    
            
            
            
