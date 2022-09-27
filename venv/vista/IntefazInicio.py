import  tkinter
from  tkinter import  *
from tkinter import filedialog
from controlador.ctrlCarga import *
from controlador.ctrlGraficas import *
from controlador.ctrlAutomata import *

class Inicio:

    def iniciar(self):
        ventana = tkinter.Tk()
        ventana.geometry("500x400")
        ventana.title("OPERACIONES ENTRE AUTOMATAS")

        menubar = Menu(ventana)
        ventana.config(menu=menubar)

        automatas = Menu(menubar, tearoff=0)
        automatas.add_command(label="Graficar", command=self.graficar)
        automatas.add_command(label="Hallar complemento", command=self.complemento)
        automatas.add_command(label="Hallar reverso",command=self.reverso)
        automatas.add_command(label="Unir automatas",command=self.unir)
        automatas.add_command(label="Hacer interseccion entre automatas",command=self.intersectar)
        automatas.add_separator()
        automatas.add_command(label="Salir", command=ventana.quit)

        menubar.add_cascade(label="AUTOMATAS", menu=automatas)


        ventana.mainloop()

    def graficar(self):
        ruta1 = ""
        ruta1 = filedialog.askopenfilename(title="Cargar automata",initialdir="C:/",filetypes=(("Archivos json","* .json")))
        if ruta1 != None:
           carga = cargaArchivo(ruta1)
           grafica = Grafica()
           grafica.graficar(carga.automata1)


    def intersectar(self):
        ruta1 = ""
        ruta2 = ""
        ruta1 = filedialog.askopenfilename(title="Cargar automata1", initialdir="C:/",
                                           filetypes=(("Archivos json", "* .json")))
        ruta2 = filedialog.askopenfilename(title="Cargar automata2", initialdir="C:/",
                                           filetypes=(("Archivos json", "* .json")))
        if ruta1 != None and ruta2 != None:
            carga = cargaArchivo(ruta1, ruta2)
            automata = Automata()
            aut = automata.interseccionAutomatas(carga.automata1, carga.automata2)
            grafica = Grafica()
            grafica.graficar(aut)

    def unir(self):
        ruta1 = ""
        ruta2 = ""
        ruta1 = filedialog.askopenfilename(title="Cargar automata1", initialdir="C:/Users/JUNIOR/Desktop/Automatas",
                                           filetypes=(("Archivos json", "* .json")))
        ruta2 = filedialog.askopenfilename(title="Cargar automata2", initialdir="C:/",
                                           filetypes=(("Archivos json", "* .json")))
        if ruta1 != None and ruta2 != None:
            carga = cargaArchivo(ruta1,ruta2)
            automata = Automata()
            aut = automata.unionAutomatas(carga.automata1,carga.automata2)
            grafica = Grafica()
            grafica.graficar(aut)

    def reverso(self):
        ruta1 = ""
        ruta1 = filedialog.askopenfilename(title="Cargar automata", initialdir="C:/",
                                           filetypes=(("Archivos json", "* .json")))
        if ruta1 != None:
            carga = cargaArchivo(ruta1)
            automata = Automata()
            aut = automata.reversoAutomata(carga.automata1)
            grafica = Grafica()
            grafica.graficar(aut)

    def complemento(self):
        ruta1 = ""
        ruta1 = filedialog.askopenfilename(title="Cargar automata", initialdir="C:/",
                                           filetypes=(("Archivos json", "* .json")))
        if ruta1 != None:
            carga = cargaArchivo(ruta1)
            automata = Automata()
            aut = automata.complementoAutomata(carga.automata1)
            grafica = Grafica()
            grafica.graficar(aut)


i = Inicio()
i.iniciar()