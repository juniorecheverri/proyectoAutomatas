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
                if (acepta == nuevo): #Si el estado está dentro de la lista de estados de aceptacion
                    posEstado = nuevos_aceptacion.index(acepta) #guarda la posicion del estado
                    nuevos_aceptacion.pop(posEstado)

        automata["F"] = nuevos_aceptacion
        print("Complemento del automata:")
        print(automata)
        
        return automata

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
        for estadosP in automata1["Q"]:  # ciclos para crear la combinacion de transiciones
            for estadosS in automata2["Q"]:
                for transicion2 in automata2["transiciones"]:  # verifica las transiciones del segundo automata
                    for transicion1 in automata1["transiciones"]:  # verifica las transiciones del primer automata
                        if transicion1[0] == estadosP and transicion2[0] == estadosS and transicion1[1] == transicion2[1]:  # verifica si hay una ruta de la cada estado con el mismo alfabeto
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

        if len(automata["F"]) == 1: #si el automata solo tiene un estado de aceptacion
            reverso = self.invertirAutomata(automata)
            return reverso
        else:
            automata["Q"].append("auxiliar") #creamos el estado auxiliar
            for estado in automata["Q"]:
                for aceptacion in automata["F"]:
                    if estado == aceptacion: #si el estado es de aceptacion
                        automata["transiciones"].append([estado, "lamda", "auxiliar"])
            automata["F"] = ["auxiliar"] #reescribo la lista de estados de aceptacion
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

        for transicion in automata["transiciones"]: #ciclo para invertir las transiciones
            reverso["transiciones"].append([transicion[2], transicion[1], transicion[0]])

        copiaAceptacion = automata["F"]
        copiaInicial = automata["Q0"]

        reverso["Q0"] = copiaAceptacion[0] #pego el estado aceptacion del automata original en el estado inicial del nuevo automata
        reverso["F"].append(copiaInicial) #pego el estado inicial del automata original en el estado de aceptacion del nuevo automata

        print("Revirtiendo el automata")
        time.sleep(1)
        print(reverso)

        return reverso

    def verificarInalcanzable(self, automata):
        encontrado = False

        nuevo = copy(automata)

        for estado in automata["Q"]:
            encontrado = False
            for transicion in automata["transiciones"]:

                if transicion[2] == estado and transicion[0] != estado and estado != automata["Q0"]:
                    encontrado = True
                    break
            if not encontrado:
                posEstado = nuevo["Q"].index(estado)
                nuevo["Q"].pop(posEstado)

                for transicion1 in automata["transiciones"]:
                    if transicion1[0] == estado:
                        posTransicion = nuevo["transiciones"].index(transicion1)
                        nuevo["transiciones"].pop(posTransicion)
        print("_______________________")
        print(nuevo)
        return nuevo