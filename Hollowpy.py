#Librerias
import pygame
import os
from pygame.locals import *


(width, height) = (680,350) # Tamaño de ventana (680,350)

background_color = (255,255,255) # Color de fondo

screen = pygame.display.set_mode((width, height)) # Aplicar tamaño a la ventana
screen.fill(background_color)  # Aplicar color a la ventana
pygame.display.set_caption('Hollowpy') #Titulo de la ventana
pygame.display.flip() # Refrescar pantalla inicial

# Coordenadas iniciales

x = 0
y = 240 


#Sprite

sprite = 0
sentido = 'N'
offset = 0
knight = []

# Variables fondo
fondo = []
Numerofondo = 0

#Salto
salto = False
tics = 0

#Imagenes

current_path = os.path.dirname(__file__) # Donde se encuentra el .py
resource_path = os.path.join(current_path, 'resources' ) # Recursos que usaremos
image_path = os.path.join(resource_path, 'images') # Imagenes dentro de recursos

#Knight
preknightD1 = pygame.image.load(os.path.join(image_path, 'Sprite1.png')) 
preknightD2 = pygame.image.load(os.path.join(image_path, 'Sprite2.png')) 
preknightD3 = pygame.image.load(os.path.join(image_path, 'Sprite3.png')) 
preknightD4 = pygame.image.load(os.path.join(image_path, 'Sprite4.png'))

preknightD5 = pygame.image.load(os.path.join(image_path, 'Sprite5.png')) 
preknightD6 = pygame.image.load(os.path.join(image_path, 'Sprite6.png')) 
preknightD7 = pygame.image.load(os.path.join(image_path, 'Sprite7.png')) 
preknightD8 = pygame.image.load(os.path.join(image_path, 'Sprite8.png'))

preknightD = [preknightD1,preknightD2,preknightD3,preknightD4,preknightD5,preknightD6,preknightD7,preknightD8]

#Sprites

for i in range (len(preknightD)):
    knight.append(pygame.transform.scale(preknightD[i],(80, 80))) 

def recorrersprites(sentido):
    global sprite
    global offset
    if sentido == 'D':
        offset = 0
    elif sentido == 'I':
        offset = 4
    if sprite <= 3:
        sprite = sprite + 1 
        if sprite == 4:
            sprite = 0
# Fin sprites 

#Salto
def saltar():
    global y
    global salto
    global tics
    if salto == False:
        tics = pygame.time.get_ticks() 
        salto = True
    y = y - 5




#Fondos
prefondo1 = pygame.image.load(os.path.join(image_path, 'Fondo.jpg')) 
prefondo2 = pygame.image.load(os.path.join(image_path, 'Fondo2.jpg')) 
prefondo3 = pygame.image.load(os.path.join(image_path, 'Fondo3.jpg')) 
prefondot = [prefondo1,prefondo2,prefondo3]
for i in range (len(prefondot)):
    fondo.append(pygame.transform.scale(prefondot[i],(680,350))) 

#Cambio de fondos
def verificarfondo():
    global x
    global y
    global Numerofondo
    if salto == False:
        if Numerofondo == 0:
            y = 240
            if x >= 620:
                Numerofondo = Numerofondo + 1
                x = 0
            elif x < 0:
                x = 0
        elif Numerofondo == 1:
            y = 247
            if x >= 620:
                Numerofondo = Numerofondo + 1
                y = 140
                x = 0
            elif x < 0:
                Numerofondo = Numerofondo - 1
                x = 620
        elif Numerofondo == 2:
            if x >= 620:
                x = 620
                y = 206
            elif x >= 0 and x <=60:
                if y > 140:
                    x = 63
                else:
                    y = 140
            elif x > 60 and x <=155:
                if y > 160:
                    x = 156
                else:
                    y = 160
            elif x > 155 and x <=255:
                if y > 185:
                    x = 256
                else:
                     y = 185
            elif x > 255 and x <620:
                y = 206
            elif x < 0:
                Numerofondo = Numerofondo - 1
                x = 620
            





#Reloj
reloj = pygame.time.Clock()

#Funcion de acciones del caballero

def accion(teclado):
    global x 
    if teclado[K_a]:
        x -= 5
        sentido = 'I'
        recorrersprites(sentido)
    if teclado[K_d]:
        sentido = 'D'
        recorrersprites(sentido)
        x += 5
    if teclado[K_SPACE]:
        saltar()
        
# Fin funcion de accion del caballero

# Mantener la pantalla
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Fin de mantener la pantalla
# Juego

    teclado = pygame.key.get_pressed() # Constantes de pygame
    """
    if teclado[K_w]:
        y -= 5
    if teclado[K_s]:
        y += 5
     """
    
    accion(teclado)
    reloj.tick(25)
    screen.fill(background_color)  # Blanquear ventana  
    if pygame.time.get_ticks() - tics > 500:
        salto = False
    verificarfondo()
    screen.blit(fondo[Numerofondo],(0,0))
    screen.blit(knight[sprite + offset],(x,y))
    pygame.display.update()
    print(x,y)


