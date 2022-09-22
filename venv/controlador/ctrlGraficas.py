import  pygame,sys
class Grafica:
    
    def pintar(self,grafo):
        pygame.init()

        color = (60, 226, 231)
        negro = (3, 3, 3)
        size = (900, 700)

        # Crear ventana
        ventana = pygame.display.set_mode(size)

        while True:
            for evet in pygame.event.get():
                if evet.type == pygame.QUIT:
                    sys.exit()
            # pitar color de fondo
            ventana.fill(color)

            # ---------- Zona de pintar------------
            font = pygame.font.SysFont("Arial", 16)
            pygame.draw.circle(ventana, negro, [200, 200], 40, 2)
            text = font.render("nombre", True, negro)
            ventana.blit(text, [200 - 20, 200 - 10])

            # actualizar fondo
            pygame.display.flip()

        

