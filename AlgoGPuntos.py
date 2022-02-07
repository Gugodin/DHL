from glob import glob
from turtle import goto
from Ind import Ind
import random  

#PARAMETROS PARA LO DE LAS CIUDADES
IntervaloX = [-3,3]
IntervaloY = [-4,4]
NoCiudades = 5
InitialCity = None
Cities = []
Population:Ind = []

#PARAMETROS PARA EL ALGORITMO GENETICO
InitialPopulation = 5
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

        print(f'Individuo {i+1}')
        print(ind.toString())




















if __name__ == '__main__':

    for i in range(numGeneration):
        Generations.update({f'gen{i+1}':[]})
    
    generateCities()

    # print(f'Ciudad inicial: {InitialCity}')
    # print(f'Ciudades: {Cities}')
    
    generatePopulation()
    # temp = [[2,1],[3,3],[7,2]]

    # print(temp.count([2,0]))