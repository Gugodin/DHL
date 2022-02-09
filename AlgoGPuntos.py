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





def cruza(parents):

    children = []

    spotCross1 = 1
    spotCross2 = len(parents[0][0].ruta) - 2
    
    for i in range(len(parents)):


        if len(parents) > 1:
            
            p1 = parents[i][0].ruta
            p2 = parents[i][1].ruta
            p1.pop(0)
            p2.pop(0)
            p1.pop(len(p1)-1)
            p2.pop(len(p2)-1)

            print(f'Padre 1 ruta: {p1}')
            print(f'Padre 2 ruta: {p2}')

            # Comenzamos con algoritmo PMX
            puntosDeCruza = []
            puntoCruza1 = random.randint(0,len(p1)-1)
            puntoCruza2 = random.randint(0,len(p1)-1)

            #Cuando se repita
            while puntoCruza2 == puntoCruza1:
                puntoCruza2 = random.randint(0,len(p1)-1)
            
            puntosDeCruza.append(puntoCruza1)
            puntosDeCruza.append(puntoCruza2)

            print(puntosDeCruza)

            cont = min(puntosDeCruza)

            child1 = []
            child2 = []
            
            while cont <= max(puntosDeCruza):
                # print(f'Intermedio de padre 2 {p1[cont]}')
                child1.append(p2[cont])
                cont+=1

            cont = min(puntosDeCruza)    

            while cont <= max(puntosDeCruza):
                # print(f'Intermedio de padre 1 {p2[cont]}')
                child2.append(p1[cont])
                cont+=1

            cp1:list = p1.copy()
            cp2:list = p2.copy()
            
            #Comparamos el hijo 1 con el padre 1

            for x in range(len(cp1)):
                elementoPadre = cp1[x]
                if child1.count(elementoPadre) == 1:
                    cp1[x] = ''
            
            for x in range(cp1.count('')):
                cp1.pop(cp1.index(''))


                
                
                    
   

            print(f'hijo 1 {child1}')
            print(f'Padre {p1}')
            print(f'Copia del padre {cp1}')



            
    







if __name__ == '__main__':

    for i in range(numGeneration):
        Generations.update({f'gen{i+1}':[]})
    
    generateCities()
    
    generatePopulation()
 


    mating()
