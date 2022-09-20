import json

class cargaArchivo():

    def cargarArchivo(self):
        automata = {}
        with open('../recursos/a.json') as archivo:
            automata = json.load(archivo)
        if(not self.verificarQuintupla(automata)):
            print("Error en la definición de la quintupla")
        else:
            print("Autómata cargado con éxito")
    
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
                
            
    
carga = cargaArchivo()
carga.cargarArchivo()