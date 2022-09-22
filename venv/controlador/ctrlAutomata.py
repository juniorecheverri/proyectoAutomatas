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

        estados = automata["Q"]
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

    def reversoAutomata(self, automata):

        print(automata)
        reverso = copy(automata)
        reverso["transiciones"]=[]
        transiciones = automata["transiciones"]
        nuevasTransiciones = []
        
        for transicion in transiciones:
            reverso["transiciones"].append([transicion[2], transicion[1], transicion[0]])


        print("reverso del automata:")
        print(reverso)

        return reverso