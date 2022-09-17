class Estado():
    def __init__(self,nombre, aceptacion, inicial):
        self.nombre = nombre
        self.aceptacion = aceptacion
        self.inicial = inicial
        self.ListaSalientes = []
        self.ListaEntrantes = []

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getListaSalientes(self):
        return self.ListaSalientes

    def setListaSalientes(self, dato):
        self.ListaSalientes.remove(dato)

    def setListaEntrantes(self, dato):
        self.ListaEntrantes.remove(dato)

    def getListaEntrantes(self):
        return self.ListaEntrantes

    def gradosalida(self):
        return len(self.ListaSalientes)