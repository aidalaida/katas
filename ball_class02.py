import pygame as pg
import sys
from random import randint, choice

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600
pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

class Bola():
    def __init__(self, x, y, vx=5, vy=5, color= (255, 255, 255), radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.anchura = radio*2
        self.altura = radio*2
    def actualizar(self):
        self.x += self.vx
        self.y += self.vy
        if self.y <=0:
            self.vy = -self.vy
        if self.x <=0 or self.x >=ANCHO:
            self.vx = -self.vx
        if self.y >=ALTO:
            self.x = ANCHO // 2
            self.y = ALTO // 2
            self.vx = randint(5,10)*choice([-1, 1])
            self.vy = randint(5,10)*choice([-1, 1])
            return True
        return False
    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.anchura//2)
    def comprueba_colision(self, objeto):
   
        choqueX = self.x >= objeto.x and self.x <= objeto.x+objeto.anchura or \
           self.x+self.anchura >= objeto.x and self.x+self.anchura <= objeto.x + objeto.anchura
        choqueY = self.y >= objeto.y and self.y <= objeto.y+objeto.altura or \
           self.y+self.altura >= objeto.y and self.y+self.altura <= objeto.y + objeto.altura
        
        if choqueX and choqueY:  #True si hay colision en x e y y hace eso
            self.vy *= -1 #cambiamos el sentido
            return True
        
        return False
class Raqueta():
    def __init__(self, x=0, y=0):
        self.altura = 10
        self.anchura = 100
        self.color = (255, 255, 255)
        self.x = (ANCHO - self.anchura) // 2
        self.y = ALTO - self.altura - 15
        self.vy = 0
        self.vx = 13
    def dibujar(self, lienzo):
        rect = pg.Rect(self.x, self.y, self.anchura, self.altura) #Así se dibuja un rectangulo, intanciarla metiendole parametros
        pg.draw.rect(lienzo, self.color, rect)
    def actualizar(self):
        teclas_pulsadas = pg.key.get_pressed() 
        #caprtuar el evneto de pulsar. Estructura de datos iterable e indexable.# ACCEDER A LOS INDICES SIEMPRE CON [].  K_LEFT es el indice del valor de la tecla
        if teclas_pulsadas[pg.K_LEFT] and self.x > 0:
            self.x -= self.vx
        if teclas_pulsadas[pg.K_RIGHT] and self.x < ANCHO - self.anchura:
            self.x += self.vx


vidas = 3
puntuacion = 0
bola = Bola(randint(0, ANCHO),
            randint(0, ALTO),
            randint(5, 10)*choice([-1, 1]),
            randint(5, 10)*choice([-1, 1]),
            AZUL)

raqueta = Raqueta()

#inicializo todo lo que quiero meter en el bucle
txtGameOver = pg.font.SysFont("Arial", 35)
txtPuntuacion = pg.font.SysFont("Courier", 28)
pierdebola = False
game_over = False

while not game_over and vidas > 0:
    v = reloj.tick(60)
    if pierdebola: #para ponerlo detras del flip, no será verdadero hasta que no se haya cerrado el bucle
        pg.time.delay(500)


    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    # Modificación de estado
    raqueta.actualizar()
    pierdebola = bola.actualizar() #compruebo si toca el fondo
    pantalla.fill(NEGRO) #limpio pantalla

    if pierdebola: #gestión de estados
        vidas -= 1
        #resetear la bola. Se juega con 
        if vidas == 0:
            texto = txtGameOver.render("GAME_OVER", True, (0, 255, 255)) #me devuelve un surface
            pantalla.blit(texto, (400,300))       
        else:
            bola.x = 400
            bola.y = 300  
            bola.dibujar(pantalla)
            raqueta.dibujar(pantalla)  
    else:
        if bola.comprueba_colision(raqueta):
            puntuacion += 5

        # Gestión de la pantalla
        texto = txtPuntuacion.render(str(puntuacion), True, (255,255,0))
        pantalla.blit(texto, (20, 20))
        bola.dibujar(pantalla)
        raqueta.dibujar(pantalla)
    
    pg.display.flip()
  
pg.time.delay(1000)
pg.quit()
sys.exit()