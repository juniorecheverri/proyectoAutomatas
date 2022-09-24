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
        transicionesReverso1 = copy(reverso["transiciones"])
        transicionesReverso2 = copy(reverso["transiciones"])
        encontrado = False
        estadosReverso = reverso["Q"]

        for rep in range(2):
            for estado in estados:
                encontrado = False
                for transicion in transicionesReverso1:
                    if transicion[2] == estado and transicion[0] != estado:
                        x = [transicion[0], transicion[1], estado]
                        if (transicion == x):
                            print("....")
                            print(x)
                            print("No es sumiedero: ", estado)
                            encontrado = True
                            break

                if not encontrado:
                    print("estado inalcanzable: ", estado)
                    for t in transicionesReverso1:
                        if t[0] == estado or t[2] == estado:
                            print(t)
                            print("___________")
                            transicionesReverso2.pop(transicionesReverso2.index(t))
                    for e in estados:
                        if e == estado:
                            estadosReverso.pop(estadosReverso.index(e))

                reverso["transiciones"] = transicionesReverso2
                transicionesReverso1 = copy(transicionesReverso2)



        print("reverso completo")
        print(reverso)

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


