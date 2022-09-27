from collections import deque
from copy import copy
import time

class Automata():

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

    def reversoAutomata(self, automata):
        print(automata)
        reverso = {}

        if len(automata["F"])==1:
            reverso = self.invertirAutomata(automata)
            return reverso

        return reverso

    def unionAutomatas(self, automata1, automata2):
        nuevoAutomata = {
                "Descripcion":"Union de 2 automatas",
                "Q":[],
                "alfabeto":[set(automata1["alfabeto"] + automata2["alfabeto"])],
                "transiciones":[],
                "Q0":"",
                "F":[]
                }
        encontrado = False
        for estadosPrimero in automata1["Q"]:   #ciclos para crear la combinacion de estados
            for estadosSegundo in automata2["Q"]:
                encontrado = False
                for estadoNuevos in nuevoAutomata["Q"]: #verifica la lista de estados nuevos
                    aux = estadosSegundo+estadosPrimero # en busca de que no exista un estado
                    if estadoNuevos == aux:             #con el mismo nombre pero inveritido
                        encontrado = True
                        break
                if not encontrado:  #Si no lo encuentra

                    nuevoAutomata["Q"].append(estadosPrimero + estadosSegundo) #agregue el nuevo estado a la lista de estados
                    if estadosPrimero == automata1["Q0"] and estadosSegundo == automata2["Q0"]:
                        nuevoAutomata["Q0"] = (estadosPrimero + estadosSegundo) #Agrega el estado de aceptacion si el nuevo estado es la combinacion de estados iniciales del primer automata y del segundo
                    for finales1 in automata1["F"]:
                        for finales2 in automata2["F"]:
                            if finales1 == estadosPrimero or finales2 == estadosSegundo:
                                nuevoAutomata["F"].append(estadosPrimero + estadosSegundo)
        #----------------------------------------
        for estadosP in automata1["Q"]:  # ciclos para crear la combinacion de estados
            for estadosS in automata2["Q"]:
                for transicion2 in automata2["transiciones"]:  # verifica las transiciones del primer automata
                    for transicion1 in automata1["transiciones"]:  # verifica las transiciones del primer automata
                        if transicion1[0] == estadosP and transicion2[0] == estadosS and transicion1[1] == transicion2[1]:  # con el mismo nombre pero inveritido
                            nuevoAutomata["transiciones"].append([estadosP + estadosS, transicion1[1], transicion1[2] + transicion2[2]])

        print(nuevoAutomata)
        return nuevoAutomata

    def interseccionAutomatas(self, automata1, automata2):
        nuevoAutomata = {
                "Descripcion":"Interseccion de 2 automatas",
                "Q":[],
                "alfabeto":[set(automata1["alfabeto"] + automata2["alfabeto"])],
                "transiciones":[],
                "Q0":"",
                "F":[]
                }
        encontrado = False
        for estadosPrimero in automata1["Q"]:   #ciclos para crear la combinacion de estados
            for estadosSegundo in automata2["Q"]:
                encontrado = False
                for estadoNuevos in nuevoAutomata["Q"]: #verifica la lista de estados nuevos
                    aux = estadosSegundo+estadosPrimero # en busca de que no exista un estado
                    if estadoNuevos == aux:             #con el mismo nombre pero inveritido
                        encontrado = True
                        break
                if not encontrado:  #Si no lo encuentra

                    nuevoAutomata["Q"].append(estadosPrimero + estadosSegundo) #agregue el nuevo estado a la lista de estados
                    if estadosPrimero == automata1["Q0"] and estadosSegundo == automata2["Q0"]:
                        nuevoAutomata["Q0"] = (estadosPrimero + estadosSegundo) #Agrega el estado de aceptacion si el nuevo estado es la combinacion de estados iniciales del primer automata y del segundo
                    for finales1 in automata1["F"]:
                        for finales2 in automata2["F"]:
                            if finales1 == estadosPrimero and finales2 == estadosSegundo:
                                nuevoAutomata["F"].append(estadosPrimero + estadosSegundo)
        #----------------------------------------
        for estadosP in automata1["Q"]:  # ciclos para crear la combinacion de estados
            for estadosS in automata2["Q"]:
                for transicion2 in automata2["transiciones"]:  # verifica las transiciones del primer automata
                    for transicion1 in automata1["transiciones"]:  # verifica las transiciones del primer automata
                        if transicion1[0] == estadosP and transicion2[0] == estadosS and transicion1[1] == transicion2[1]:  # con el mismo nombre pero inveritido
                            nuevoAutomata["transiciones"].append([estadosP + estadosS, transicion1[1], transicion1[2] + transicion2[2]])

        print(nuevoAutomata)
        return nuevoAutomata

    def reversoAutomata(self, automata):
        print(automata)
        reverso = {}

        if len(automata["F"]) == 1:
            reverso = self.invertirAutomata(automata)
            return reverso
        else:
            automata["Q"].append("auxiliar")
            for estado in automata["Q"]:
                for aceptacion in automata["F"]:
                    if estado == aceptacion:
                        automata["transiciones"].append([estado, "lamda", "auxiliar"])
            automata["F"] = ["auxiliar"]
            reverso = self.invertirAutomata(automata)
            return reverso
        return reverso

    def invertirAutomata(self, automata):

        reverso = {"Descripcion":"Inverso del automata",
                "Q":[],
                "alfabeto":[],
                "transiciones":[],
                "Q0":"",
                "F":[]}
        reverso["Q"] = automata["Q"]
        reverso["alfabeto"] = automata["alfabeto"]

        for transicion in automata["transiciones"]:
            reverso["transiciones"].append([transicion[2], transicion[1], transicion[0]])

        copiaAceptacion = automata["F"]
        copiaInicial = automata["Q0"]

        reverso["Q0"] = copiaAceptacion[0]
        reverso["F"].append(copiaInicial)

        print("Revirtiendo el automata")
        time.sleep(1)
        print(reverso)

        return reverso