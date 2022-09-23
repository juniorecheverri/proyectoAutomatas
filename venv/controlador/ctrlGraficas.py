import  pygame,sys

class Grafica():
    
    def pintar(self,automata):
        pygame.init()

        color = (60, 226, 231)
        negro = (3, 3, 3)
        size = (900, 700)
        estados = self.getEstados(automata)

        # Crear ventana
        ventana = pygame.display.set_mode(size)

        while True:
            for evet in pygame.event.get():
                if evet.type == pygame.QUIT:
                    sys.exit()
            # pitar color de fondo
            ventana.fill(color)

            # ---------- Zona de pintar------------
            for estado in estados:
                font = pygame.font.SysFont("Arial", 16)
                pygame.draw.circle(ventana, negro,estado["coordenadas"], 40, 2)
                text = font.render(estado["nombre"], True, negro)
                ventana.blit(text, [(estado["coordenadas"][0]-20), (estado["coordenadas"][1] - 10)])

            # actualizar fondo
            pygame.display.flip()

    def getEstados(self,automata):
        estados = automata["Q"]
        EstadosCoordenada = []
        i = 0
        for e in estados:
            i+=1
            EstadosCoordenada.append({"nombre":e,"coordenadas":[(110*i),(110*i)]})

        return EstadosCoordenada


