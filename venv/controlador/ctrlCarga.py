import json
import time
from controlador.ctrlAutomata import *
from controlador.ctrlGraficas import Grafica

class cargaArchivo():

    def cargarArchivo(self):
        automata = {}
        with open('../recursos/no_ceros.json') as archivo:
            automata = json.load(archivo)
        if(not self.verificarQuintupla(automata)):
            print("Error en la definición de la quintupla")
        else:
            automata = self.verificarCompleto(automata)
            print("Autómata cargado con éxito")
            return self.main(automata)
        return automata
    
    def verificarQuintupla(self, automata):
        if(not automata["Q0"] and automata["Q0"] == ""):
            return False
        elif(not automata["alfabeto"] and automata["alfabeto"] == []):
            return False
        elif(not automata["Q"] and automata["Q"] == [] and len(automata["Q"])>4):
            return False
        elif (not automata["F"] and automata["F"] == []):
            return False
        elif (not automata["transiciones"] and automata["trancisiones"] == []):
            return False
        elif (not self.verificarTransiciones(automata["transiciones"], automata["Q"], automata["alfabeto"])):
            return False
        return True
        
    def verificarTransiciones(self, transiciones, estados, alfabeto):
       for transicion in transiciones:
            tamTransicion = len(transicion)
            if(tamTransicion != 3):
                print("Transición incorrecta")
                return False
            else:
                inicial = transicion[0]
                final = transicion[2]
                letra = transicion[1]

                if(not self.buscarEstado(inicial, estados) or not self.buscarEstado(final, estados)):
                    print("Uno de los estados no existe")
                    return False
                if(not self.buscarAlfabeto(letra, alfabeto)):
                    print("Uso incorrecto del alfabeto")
                    return False
            return True
        
    def verificarCompleto(self, automata):
        if(len(automata["Q"])*len(automata["alfabeto"]) == len(automata["transiciones"])):
            print("El autómata es completo")
            return automata
        else:
            print("Automata incompleto")
            print("completando el automata")
            time.sleep(3)

            automata["Q"].append("sumidero")
            a_completo = self.buscarYcompletar(automata)

            print(a_completo)
            return a_completo

        
                
    def buscarEstado(self, estado, lista):
        for a in lista:
            if (a == estado):
                return True
        return False

    def buscarAlfabeto(self, letra, alfabeto):
        for a in alfabeto:
            if (a == letra):
                return True
        return False

    def buscarYcompletar(self, automata):
    #Función para completar un automata
        alfabeto = automata["alfabeto"]
        estados = automata["Q"]
        transiciones = automata["transiciones"]

        encontrado = False
        for inicial in range(len(estados)):
            for letra in range(len(alfabeto)):
                encontrado = False
                for transicion in range(len(transiciones)):
                    x=[estados[inicial],alfabeto[letra],transiciones[transicion][2]]
                    print(x)
                    if(transiciones[transicion] == x):
                        print("....")
                        print("Encontrado: ", x)
                        encontrado = True
                        break
                if (not encontrado):
                    automata["transiciones"].append([estados[inicial], letra, "sumidero"])
                    print("llorelo mi pez")
                    print("aaaaaaahhhh, te creas, ya te lo actualizo mi rey" )
        return automata

    def main(self, automata):
        ctrl = Automata()
        grafica = Grafica()
        print("LISTA DE OPCIONES")

        opcion = int(input("--------------------------\n"
                    "Selecciona una opcion:\n"
                    "0. SALIR\n"
                    "1. Graficar\n"
                    "2. Hallar complemento\n"
                    "3. Hallar reverso\n"
                    "--------------------------\n"))
        if (opcion == 1):  # complemento

            grafica.pintar(automata)

        if (opcion == 2):  # complemento
            return ctrl.complementoAutomata(automata)

        elif (opcion == 3):  # reverso
            return ctrl.reversoAutomata(automata)
        elif (opcion == 0):  # reverso
            return automata
        return automata

carga = cargaArchivo()
carga.cargarArchivo()