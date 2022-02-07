from math import sqrt

KM = 5.9
GAS = 22.16

class Ind:

    def __init__(self,ruta):   
        self.ruta = ruta
        self.distancias = []
        self.generateDataInd()
    

    def generateDataInd(self):

        #Calculamos el numero de distancias que tendra la ruta
        noDistancias= len(self.ruta) - 1

        for i in range(noDistancias):
            #Tomamos las dos ciudades a calcular la distancia

            city1 = self.ruta[i]
            city2 = self.ruta[i+1]

            distancia = round(sqrt((city2[0]-city1[0])**2 + (city2[1]-city1[1])**2),4)

            self.distancias.append(distancia)

        self.distanciaTotal = round(sum(self.distancias),1)

        self.litrosGas = round(self.distanciaTotal/KM,2)

        self.gasto = round(self.litrosGas * GAS,2)



        

    def toString(self):
        return f'Ruta: {self.ruta} \nDistancias: {self.distancias}\nTotal de distancia: {self.distanciaTotal}\nLitros: {self.litrosGas}\nGasto: {self.gasto}'

