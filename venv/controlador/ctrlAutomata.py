from collections import deque
from copy import copy

class Automata():

    def __init__(self):
        self.ListaEstados = []
        self.alfabeto = []
        self.transiciones = []
        self.inicial: ""
        self.aceptacion: []
        
    def complementoAutomata(self, automata):
        print(automata)

        estados = copy(automata["Q"])
        aceptacion = automata["F"]
        nuevos_aceptacion = automata["Q"]

        for acepta in aceptacion:
            for nuevo in estados:
                print(acepta)
                if (acepta == nuevo):
                    posEstado = nuevos_aceptacion.index(acepta)
                    nuevos_aceptacion.pop(posEstado)

        automata["F"] = nuevos_aceptacion
        print("Complemento del automata:")
        print(automata)
        
        return automata
    
    def reverso2(self,automata):
        automata1 = self.cambiarDireciones(automata)
        self.getSumidero(automata1)
        sumideros = self.getSumidero(automata1)
        print(sumideros)
    
    def cambiarDireciones(self,automata):
        print(automata)
        reverso = copy(automata)
        reverso["transiciones"] = []
        transiciones = automata["transiciones"]
        estados = reverso["Q"]

        for transicion in transiciones:
            reverso["transiciones"].append([transicion[2], transicion[1], transicion[0]])

        return reverso
    
    def getSumidero(self,automata):
        estados = automata["Q"]
        transiciones = automata["transiciones"]
        count = 0
        count2 = 0
        sumideros = []
        for estado in estados:
            for trasicion in transiciones:
                if(estado == trasicion[2]):
                    if(trasicion[0] == estado):
                        count +=1
                    count2 +=1
            if(count <= 2):
                conut3 = count +count2
                if(conut3 > 2):
                    return None
                else:
                    sumideros.append(estado)
                    return sumideros
        return  None

        
        print(transiciones)
        

    def reversoAutomata(self, automata):
        print(automata)
        reverso = copy(automata)
        reverso["transiciones"] = []
        transiciones = automata["transiciones"]
        estados = reverso["Q"]

        for transicion in transiciones:
            reverso["transiciones"].append([transicion[2], transicion[1], transicion[0]])

        print("reverso del automata:")

        print(reverso)
        transicionesReverso = reverso["transiciones"]
        encontrado = False
        estadosReverso = reverso["Q"]
        for estado in estados:
            print(estado)
            encontrado = False
            for transicion in transicionesReverso:
                if transicion[2] == estado and transicion[0] != estado:
                    x = [transicion[0], transicion[1], estado]
                    if (transicion == x):
                        print("....")
                        print(x)
                        print("No es sumiedero: ", estado)
                        encontrado = True
                        break
            if (not encontrado):
                for e in estados:
                    if e == estado:
                        estadosReverso.pop(estadosReverso.index(e))



        print("reverso completo")
        print(reverso)

