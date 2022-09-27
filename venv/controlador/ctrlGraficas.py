import matplotlib.pyplot as plt
import networkx as nx
import copy


class Grafica():

    def graficar(self,automata):
        aut = automata
        transiciones = aut["transiciones"]
        # Instantiate the DiGraph
        G = nx.DiGraph()
        relacionesInversas = []
        inicial = aut["Q0"]
        acep = aut["F"]
        estados = aut["Q"]
        #nodos que no son el inicial ni de aceptacion
        NINA = self.noInicialNoaceptacion(inicial,acep,estados)
        # agregando transiciones
        for transicion in transiciones:
            origen = transicion[0]
            destino = transicion[2]
            alfabeto = transicion[1]
            relacionesInversas.append([destino,alfabeto,origen])
            doble = self.getTransicionDoble(relacionesInversas,transicion)
            if doble:
                origen = doble[0]
                destino=doble[2]
                alfabeto = doble[1]
               # print(doble)
            self.agregar_arista(G, origen, destino, alfabeto)

        # Draw the netwo

        pos = nx.layout.planar_layout(G)
        options1 = {"node_size": 1200, "node_color": "y"}
        nx.draw_networkx(G, pos, nodelist=acep, **options1)

        options4 = {"node_size": 800, "node_color": "b"}
        nx.draw_networkx_nodes(G, pos, nodelist=acep, **options4)

        options3 = {"node_size": 800, "node_color": "b"}
        nx.draw_networkx_nodes(G, pos,nodelist=NINA,**options3)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title(" {0} ".format(aut["Descripcion"]))

        options = {"node_size": 900, "node_color": "g"}
        nx.draw_networkx_nodes(G, pos, nodelist=[inicial], **options)
        plt.show()

    def getTransicionDoble(self,tracionesInversas,trasicion):
        origenN = trasicion[0]
        destinoN = trasicion[2]
        datoN = trasicion[1]

        for inversa in tracionesInversas:
            origenI = inversa[0]
            destinoI = inversa[2]
            datoI = inversa[1]
            if origenI == origenN and destinoI == destinoN:
                return [origenN,"{0},{1}".format(datoN,datoI),destinoN]





    def noInicialNoaceptacion(self,inicial,aceptacio,estados):
        lista = []
        for estado in estados:
            if estado != inicial and aceptacio.count(estado) == 0:
                lista.append(estado)
        return lista

    def agregar_arista(self,G, u, v, w=1):
        G.add_edge(u, v, weight=w)






