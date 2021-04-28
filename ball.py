import pygame as pg
import sys
import random

def rebotaX(x):
    if x <=0 or x>=ANCHO:
        return -1
    return 1

def rebotaY(y):
    if y <=0 or y >=ALTO:
        return -1 #multiplicar con la velocidad
    return 1

ROJO = (255, 0, 0) #parametros constantes, por si se tiene que modificar
AZUL = (0,0, 255)
VERDE = (0,255,0)
NEGRO = (0,0,0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO))
reloj = pg.time.Clock() #Instanciando un objeto del tipo clock

#Bola 1
x = ANCHO // 2
y = ALTO // 2 #División ENTEROS
vx = -7 #velocidad de la bola, se inicializa pero es inconstante
vy = -7

#Bola 2

x2 = random.randint(0, ANCHO)
y2 = random.randint(0, ALTO)
vx2 = random.randint(5, 15)
vy2 = random.randint(5, 15)

game_over = False
while not game_over:
    reloj.tick(60) #para ralentizar el movimiento, con 60 veces por segundo
    #Gestión de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla.fill(NEGRO) #rellenar la pantalla cada vez qeu se cambia
    pg.draw.circle(pantalla, ROJO, (x,y), 10)
    pg.draw.circle(pantalla, VERDE, (x2,y2), 10)
    x += vx
    y += vy

    x2 += vx2
    y2 += vy2

    vy *= rebotaY(y)
    vx *= rebotaX(x)

    vy2 *= rebotaY(y2)
    vx2 *= rebotaX(x2)

    #if y <= 0 or y >= ALTO : #con números impares o con multiplos ponemos condiciones >= o <=
       # vy = -vy
    #if x <= 0 or x >= ANCHO: #Es bueno usar operadores lógicos si es una misma condición
        #3vx = -vx
    

    pg.display.flip() #refresca pantalla

pg.quit()
sys.exit()