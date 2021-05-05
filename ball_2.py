import pygame as pg
import sys
from random import randint, choice

ANCHO = 800
ALTO = 600
FPS = 60

class Marcador():
    def __init__(self, x, y, fontsize=25, color=(255,255,255)):
        self.fuente = pg.font.SysFont("Arial", fontsize)
        self.x = x
        self.y = y
        self.color= color
    
    def dibuja(self,text, lienzo):
        image = self.fuente.render(str(text), True, self.color) #render para transformar hacia una surface
        lienzo.blit(image, (self.x, self.y)) #linezo es igual a otra surface



#Toda la geometria en el RECT
class Bola(pg.sprite.Sprite): #va a hredar de la clase SPRite. Objeto visual. sprite es el modulo de la clase SPRITE
    def __init__(self, x, y): #Crear bola y su posicion. RECT ES UNA INSTANCIA DE UN RECTANGULO
        super().__init__() #inicializar la clase SPRITE
         # o se puede hacer asi: pg.sprite.Sprite.__init__(self) #lo invoco directamente, utilizando la clase, constructor y llamar así misma, self.
        self.image= pg.image.load('./images/ball1.png').convert_alpha() #devuelve un surface/ calcomonia #convert alpha para aplicar la transparencia
        self.rect = self.image.get_rect(center = (x, y)) #DAME EL RECTANGULO DE TU IMG. Se utiliza mucho para tener la geometria del sprite. CENTER para centrarlo. Se gestiona todo a través del rectangulo

       
        self.vx = randint(5,10)*choice([-1, 1]) #lo pide nuestra bola
        self.vy = randint(5,10)*choice([-1, 1])

    def update(self): # actualizar con el codigo que lleve dentro.
        self.rect.x += self.vx #para que se mueva
        self.rect.y += self.vy

        if self.rect.left <= 0 or self.rect.right >= ANCHO: #marcar los limites y los bordes para que REBOTE.
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.vy *= -1


class Game(): #clase controlador
    def __init__(self): #Donde definimos todo lo que necesitamos, siendo un atributo
        self.pantalla =  pg.display.set_mode((ANCHO, ALTO))
        self.botes = 0
        self.cuentaGolpes = Marcador(10,10)

        self.ballGroup = pg.sprite.Group() #Llamas a un grupo de Bolas
        for i in range (randint(1,20)):
            bola = Bola(randint(0, ANCHO), randint(0,ALTO))
            self. ballGroup.add(bola) #lo meto en un grupo

       #self.bola = Bola(ANCHO//2, ALTO//2) #x,y, se la asigna en el centro, en la instancia de rect de la instancia de Bola

    def bucle_principal(self):
        game_over = False #solo tiene sentido en el bucle ppal
        reloj = pg.time.Clock()
        while not game_over:
            reloj.tick(FPS)

            for evento in pg.event.get(): #control eventos
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.ballGroup.update() #llama al metodo update de cada una de las bolas del grupo
                        
            #self.bola.update() #se actualiza permanentemente el rectangulo de la bola

            #DIBUJAR
            self.pantalla.fill((0,0,0))
            self.cuentaGolpes.dibuja('Hola', self.pantalla)
            self.ballGroup.draw(self.pantalla) #Sino lo dibujo llama a la clase padre
            #self.pantalla.blit(self.bola.image, self.bola.rect.topleft) #Siempre el blit se hace en la esquina superior izq. y espera el topleft y luego con la infotmación del rect lo centra

            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()