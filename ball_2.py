import pygame as pg
import sys
from random import randint, choice

ANCHO = 800
ALTO = 600
FPS = 60

class Marcador(pg.sprite.Sprite):
    def __init__(self, x, y, fontsize=25, color=(255,255,255)):
        super().__init__()
        self.fuente = pg.font.SysFont("Arial", fontsize)
        self.text = 0
        self.color= color
        self.image = self.fuente.render(str(self.text), True, self.color) #render para transformar hacia una surface
        self.rect = self.image.get_rect(topleft=(x,y)) #con get se coge una instancia de rectangulo
    
    def update(self, x, y, w=100, h=30): #sin update no actualizas, metodo que le grupo ya tiene
        self.image = self.fuente.render(str(self.text), True, self.color) #str convierte text en cadena    
        
class Raqueta(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((w, h), pg.SCARALPHA, 32) # superfice que aguanta transparencias con SCARALPHA con un ancho y un alto
        pg.draw.rect(self.image, (255, 0, 0), pg.Rect(0,0, w, h), border_radius=5) #esto lo dibuja encima de self.image
        self.rect = self.imagen.get_rect(centerx = x, bottom = y)
        self.vx = 7

    def update(self):
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT]:
            self.rect.x -= self.vx #para que se muevan
            

    
        

#Toda la geometria en el RECT
class Bola(pg.sprite.Sprite): #va a hredar de la clase SPRite. Objeto visual. sprite es el modulo de la clase SPRITE
    def __init__(self, x, y): #Crear bola y su posicion. RECT ES UNA INSTANCIA DE UN RECTANGULO
        super().__init__() #inicializar la clase SPRITE
         # o se puede hacer asi: pg.sprite.Sprite.__init__(self) #lo invoco directamente, utilizando la clase, constructor y llamar así misma, self.
        self.image= pg.image.load('./images/ball1.png').convert_alpha() #devuelve un surface/ calcomonia #convert alpha para aplicar la transparencia
        self.rect = self.image.get_rect(center = (x, y)) #DAME EL RECTANGULO DE TU IMG. Se utiliza mucho para tener la geometria del sprite. CENTER para centrarlo. Se gestiona todo a través del rectangulo con sus coordenadas

       
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
        self.cuentaSegundos = Marcador(10,10)

        self.todoGroup = pg.sprite.Group() #Llamas a un grupo de Bolas
        for i in range (randint(1,20)):
            bola = Bola(randint(0, ANCHO), randint(0,ALTO))
            self. todoGroup.add(bola) #lo meto en un grupo
        self.todoGroup.add(self.cuentaSegundos)

       #self.bola = Bola(ANCHO//2, ALTO//2) #x,y, se la asigna en el centro, en la instancia de rect de la instancia de Bola

    def bucle_principal(self):
        game_over = False #solo tiene sentido en el bucle ppal
        reloj = pg.time.Clock()
        contador_milisegundos = 0
        contador_segundos = 0
        while not game_over:
            dt =reloj.tick(FPS)
            contador_milisegundos += dt
            
            if contador_milisegundos >= 1000:
                contador_segundos += 1
                contador_milisegundos = 0

            for evento in pg.event.get(): #control eventos
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.cuentaSegundos.text = contador_segundos
            self.todoGroup.update() #llama al metodo update de cada una de las bolas del grupo
                        
            #self.bola.update() #se actualiza permanentemente el rectangulo de la bola

            #DIBUJAR
            self.pantalla.fill((0,0,0))
            self.todoGroup.draw(self.pantalla) #Sino lo dibujo llama a la clase padre
            #self.pantalla.blit(self.bola.image, self.bola.rect.topleft) #Siempre el blit se hace en la esquina superior izq. y espera el topleft y luego con la infotmación del rect lo centra

            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()