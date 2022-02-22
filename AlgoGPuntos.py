import sys
from PySide6.QtCore import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from Ind import Ind
import random
import cruza as repro
from PySide6.QtWidgets import *
from view.PrimeraVentana import Ui_MainWindow

# from main import ventana

# PARAMETROS PARA LO DE LAS CIUDADES
IntervaloX = [-3, 3]
IntervaloY = [-4, 4]
NoCiudades = 6
InitialCity = None
Cities = []
Population = []

# PARAMETROS PARA EL ALGORITMO GENETICO
InitialPopulation = 6
MaxPopulation = 10
ProbMutation = 0.5
ProbMutationGen = 0.05
numGeneration = 20
Generations = {}


def generateCities():
    global InitialCity

    # Generando las ciudades al azar

    i = 0
    while (i < NoCiudades):
        currentCity = []

        randX = random.randint(IntervaloX[0], IntervaloX[1])
        randY = random.randint(IntervaloY[0], IntervaloY[1])

        currentCity.append(randX)
        currentCity.append(randY)

        if Cities.count(currentCity) == 0:
            Cities.append(currentCity)
            i += 1

    # Tomando un numero random entre 0 y el total de ciudades para generar la ciudad inicial

    InitialCity = Cities[random.randint(0, len(Cities) - 1)]


def generatePopulation():
    # Generamos una lista temporal de las ciudades para poder hacerle modificaciones
    citiesToAdd = Cities.copy()

    # Sacamos la ciudad inicial del la lista temporal para no volverla agregarla
    citiesToAdd.pop(citiesToAdd.index(InitialCity))

    for i in range(InitialPopulation):

        currentCities = citiesToAdd.copy()

        # Colocamos la ruta de cada individuo
        currentRuta = [InitialCity, InitialCity]

        # Toma numeros randoms entre los index de currentCities
        for x in range(len(currentCities)):
            city = currentCities.pop(random.randint(0, len(currentCities) - 1))
            currentRuta.insert(1, city)

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

    # Generamos parejas de 2 o 1 aleatoriamente

    while len(pTemp) != 0:

        partner1 = pTemp.pop(random.randint(0, len(pTemp) - 1))

        if len(pTemp) != 0:
            partner2 = pTemp.pop(random.randint(0, len(pTemp) - 1))
            parents.append([partner1, partner2])
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
            p1.pop(len(p1) - 1)
            p2.pop(len(p2) - 1)

            ch1, ch2 = repro.pmx(p1, p2)

            ch1.insert(0, InitialCity)
            ch2.insert(0, InitialCity)
            ch1.insert(len(ch1), InitialCity)
            ch2.insert(len(ch2), InitialCity)

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


class Ventana(QMainWindow):
    listaPermisos = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generateMap)

    def generateMap(self):
        global IntervaloX
        global IntervaloY
        global NoCiudades

        xTemp = []
        yTemp = []

        xTemp.append(int(self.ui.x1.text()))
        xTemp.append(int(self.ui.x2.text()))

        yTemp.append(int(self.ui.y1.text()))
        yTemp.append(int(self.ui.y2.text()))

        xTemp = sorted(xTemp)
        yTemp = sorted(yTemp)

        IntervaloX = xTemp.copy()
        IntervaloY = yTemp.copy()
        NoCiudades = int(self.ui.nuCiudades.text())

        generateCities()

        # print(Cities)

        self.generateFirtsMap()

        plt.show()

        generatePopulation()
        
        for i in range(numGeneration):

            mating()

            if len(Population) > MaxPopulation:
                poda()

            Generations[f'gen{i+1}'] = Population.copy()

        self.generateLastMap()
        self.generateLastMap2()


    def generateFirtsMap(self):

        figure2 = plt.figure(figsize=(15, 10))

        ax = plt.subplot(1,1,1)

        ax.set_title('Mapa de ciudades generadas')

        ax.plot(IntervaloX[0], IntervaloY[0], marker='o', lw=0, visible=False)
        ax.plot(IntervaloX[1], IntervaloY[1], marker='o', lw=0, visible=False)


        for x in range(len(Cities)):

            ax.plot(Cities[x][0], Cities[x][1], marker='o', lw=0)

        ax.plot(InitialCity[0], InitialCity[1], marker='x', lw=0,color='k')


    def generateLastMap(self):

        figure2 = plt.figure(figsize=(15, 10))

        ax = plt.subplot(2, 1, 1)

        ax.set_title('Mapa de ruta')

        aptitudes = []

        for i in range(len(Generations[f'gen{numGeneration}'])):
            aptitudes.append(Generations[f'gen{numGeneration}'][i].gasto)

        print(aptitudes)
        ind = Generations[f'gen{numGeneration}'][aptitudes.index(min(aptitudes))]
        xs = []
        ys = []

        for i in range(len(ind.ruta)):
            xs.append(ind.ruta[i][0])
            ys.append(ind.ruta[i][1])

        ax.plot(xs, ys, marker='o',lw=0)

        for i in range(len(ind.ruta)-1):

            ax.annotate(' ', xy=(ind.ruta[i+1][0], ind.ruta[i+1][1]), xytext=(ind.ruta[i][0],ind.ruta[i][1]),
                arrowprops=dict(facecolor='black', shrink=0.02,width=1,headwidth=8),
                )



        ax.plot(InitialCity[0], InitialCity[1], marker='x', lw=0,color='k')

        temp = Generations[f'gen{numGeneration}'].copy()
        bestInd = [['Total Distancia','Litros','Gasto']]
        
        bestTemp = temp[aptitudes.index(min(aptitudes))]
        aptitudes.pop(aptitudes.index(min(aptitudes)))
        bestInd.append([f'{bestTemp.distanciaTotal} km', f'{bestTemp.litrosGas} litros', f'{bestTemp.gasto} pesos']) 
        
        ax2 = plt.subplot(2,1,2)
        ax2.axis('tight')
        ax2.axis('off')
        table = ax2.table(cellText = bestInd, loc = 'center', cellLoc = 'center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1,3)

        ax2.set_title(f'\n Tabla de mejor individuo\nRuta: {bestTemp.ruta}')
        


        plt.show()

    def generateLastMap2(self):

        figure2 = plt.figure(figsize=(15, 10))

        ax = plt.subplot(2, 1, 1)

        ax.set_title('Mapa de la peor ruta')

        aptitudes = []

        for i in range(len(Generations['gen1'])):
            aptitudes.append(Generations['gen1'][i].gasto)
        
        print(aptitudes)

        ind = Generations[f'gen1'][aptitudes.index(max(aptitudes))]
        
        print(ind.gasto)
        xs = []
        ys = []

        for i in range(len(ind.ruta)):
            xs.append(ind.ruta[i][0])
            ys.append(ind.ruta[i][1])

        ax.plot(xs, ys, marker='o',lw=0)

        for i in range(len(ind.ruta)-1):

            ax.annotate(' ', xy=(ind.ruta[i+1][0], ind.ruta[i+1][1]), xytext=(ind.ruta[i][0],ind.ruta[i][1]),
                arrowprops=dict(facecolor='black', shrink=0.02,width=1,headwidth=8),
                )



        ax.plot(InitialCity[0], InitialCity[1], marker='x', lw=0,color='k')

        temp = Generations[f'gen{numGeneration}'].copy()
        bestInd = [['Total Distancia','Litros','Gasto']]
        
        bestTemp = temp[aptitudes.index(min(aptitudes))]
        aptitudes.pop(aptitudes.index(min(aptitudes)))
        bestInd.append([f'{ind.distanciaTotal} km', f'{ind.litrosGas} litros', f'{ind.gasto} pesos']) 
        
        ax2 = plt.subplot(2,1,2)
        ax2.axis('tight')
        ax2.axis('off')
        table = ax2.table(cellText = bestInd, loc = 'center', cellLoc = 'center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1,3)

        ax2.set_title(f'\n Tabla del peor individuo\nRuta: {ind.ruta}')
        


        plt.show()








if __name__ == '__main__':

    for i in range(numGeneration):
        Generations.update({f'gen{i + 1}': []})

    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec())
