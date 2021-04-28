import pygame as pg
import sys

pg.init() #función constructora
pantalla = pg.display.set_mode((600, 400)) #se mete en una tupla
pg.display.set_caption("Hola")

game_over = False

while not game_over:
    #Gestión de eventos. se van acumulando y Cada vez que pasa el evento se vacia.
    for evento in pg.event.get(): 
        if evento.type == pg.QUIT:
            game_over = True

    #Gestión del estado
    print("Hola mundo")

    #Refresca pantalla

    pantalla.fill((0,255,0))

    pg.display.flip() #pasa directamente a la memoria gráfica, cogiendod el pantalla fill
pg.quit()
sys.exit()