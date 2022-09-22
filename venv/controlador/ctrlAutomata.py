from collections import deque
from modelo.Estado import *
from modelo.Arista import *
from copy import copy

class Automata():

    def __init__(self):
        self.ListaEstados = []
        self.alfabeto = []
        self.transiciones = []
        self.inicial: ""
        self.aceptacion: []
        
    def complementoAutomata(self, estados, aceptacion):

        copiaEstados = estados

        for i in range(len(estados)):
            for j in range (len(aceptacion)):
                if estados[i] == aceptacion[j]:
                    copiaEstados.pop(estados[j])

        aceptacion = copiaEstados
        return aceptacion

    def inversoAutomata(self, listaEstados, alfabeto, transiciones, inicial, aceptacion):
        