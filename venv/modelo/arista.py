class Arista():
    def __init__(self, origen, destino, dato):
        self.origen = origen
        self.destino = destino
        self.dato = dato
        
    def getOrigen(self):
        return self.origen

    def setOrigen(self,origen):
        self.origen = origen
    
    def getDestino(self):
        return self.destino

    def setDestino(self,destino):
        self.destino=destino
    
    def getDato(self):
        return self.dato

    def setDato(self,dato):
        self.dato=dato



