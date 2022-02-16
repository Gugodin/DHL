from glob import glob
import re
from turtle import goto
from Ind import Ind
import random  
import cruza as repro

#PARAMETROS PARA LO DE LAS CIUDADES
IntervaloX = [-3,3]
IntervaloY = [-4,4]
NoCiudades = 6
InitialCity = None
Cities = []
Population = []

#PARAMETROS PARA EL ALGORITMO GENETICO
InitialPopulation = 6
MaxPopulation =10
ProbMutation = 0.5
ProbMutationGen = 0.05
numGeneration = 5
Generations = {}





def generateCities ():
    global InitialCity

    #Generando las ciudades al azar

    i = 0
    while(i < NoCiudades):
        currentCity = []

        randX = random.randint(IntervaloX[0],IntervaloX[1])
        randY = random.randint(IntervaloY[0],IntervaloY[1])

        currentCity.append(randX)
        currentCity.append(randY)

        
        if Cities.count(currentCity) == 0:
            Cities.append(currentCity)
            i += 1
        

    #Tomando un numero random entre 0 y el total de ciudades para generar la ciudad inicial

    InitialCity = Cities[random.randint(0,len(Cities)-1)]





def generatePopulation():

    #Generamos una lista temporal de las ciudades para poder hacerle modificaciones
    citiesToAdd = Cities.copy()

    #Sacamos la ciudad inicial del la lista temporal para no volverla agregarla
    citiesToAdd.pop(citiesToAdd.index(InitialCity))
     
    for i in range(InitialPopulation):

        currentCities = citiesToAdd.copy()

        #Colocamos la ruta de cada individuo
        currentRuta = [InitialCity,InitialCity]
        
        # Toma numeros randoms entre los index de currentCities
        for x in range(len(currentCities)):
            city = currentCities.pop(random.randint(0,len(currentCities)-1))
            currentRuta.insert(1,city)

        ind = Ind(currentRuta)

        Population.append(ind)

        # print(f'Individuo {i+1}')
        # print(ind.toString())





def mating():

    global Population

    pTemp = []

    for i in range(len(Population)):
        pTemp.append(Population[i])

    
    parents = []
    
    #Generamos parejas de 2 o 1 aleatoriamente

    while len(pTemp) != 0:

        partner1 = pTemp.pop(random.randint(0,len(pTemp)-1))

        if len(pTemp) != 0:
            partner2 = pTemp.pop(random.randint(0,len(pTemp)-1))
            parents.append([partner1,partner2])
        else:
            parents.append([partner1])


    children = cruza(parents)

    for child in children:
        Population.append(child)





def cruza(parents):

    children = []
    
    for i in range(len(parents)):


        if len(parents) > 1:
            
            p1 = parents[i][0].ruta.copy()
            p2 = parents[i][1].ruta.copy()

        
            p1.pop(0)
            p2.pop(0)
            p1.pop(len(p1)-1)
            p2.pop(len(p2)-1)     

            ch1,ch2 = repro.pmx(p1,p2)


            ch1.insert(0,InitialCity)
            ch2.insert(0,InitialCity)
            ch1.insert(len(ch1),InitialCity)
            ch2.insert(len(ch2),InitialCity)

            # print(f'Ciudad inicial {InitialCity}')

            

            child1 = Ind(ch1)
            child2 = Ind(ch2)

            children.append(child1)
            children.append(child2)
    
    return children

           

def poda():
    global Population

    numEliminations = len(Population) - MaxPopulation

    aptitudes = []
    
    for i in range(len(Population)):
        aptitudes.append(Population[i].gasto)

    for i in range(numEliminations):
    
        for x in range(len(aptitudes)):

            if aptitudes[x] == max(aptitudes):
                Population.pop(x)
                aptitudes.pop(x)
                break

            
    







if __name__ == '__main__':

    for i in range(numGeneration):
        Generations.update({f'gen{i+1}':[]})
    
    generateCities()
     
    generatePopulation()

    for i in range(numGeneration):

        mating()

        if len(Population) > MaxPopulation:
            poda()

        Generations[f'gen{i+1}'] = Population.copy()
        

    print(Generations)


    
