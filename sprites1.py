import pygame
import random
import sys
#render es para agregar texto

ALTO=450
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AZUL=(59,131,189)
centro=[ANCHO/2,ALTO/2]
class Jugador(pygame.sprite.Sprite):
    def __init__(self,an,al,m):
        pygame.sprite.Sprite.__init__(self)
        self.dir=0
        self.x=0
        self.image=m[self.dir][self.x]
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
    def update(self):
        if self.x<=2:
            self.x+=1
        else:
            self.x=0
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=0
        if self.rect.x<=0:
            self.rect.x=0
            self.var_x=0
        if self.rect.y>=ALTO-self.rect[3]:
            self.var_y=0
        if self.rect.y<=0:
            self.var_y=0

def sacar_pixel(imagen):
    ancho_img,alto_img=imagen.get_size()
    matriz=[]
    matriz = [None] * 8
    for i in range(8):
        matriz[i] = [None] * 12
    for j in range (8):
        for i in range (12):
            cuadro = (i*32,j*32, 32, 32)
            recorte=imagen.subsurface(cuadro)
            matriz[j][i]=recorte
    return matriz


def main(recordper):
    pygame.init()
    pygame.display.set_caption('Cube Shoot')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(NEGRO)
    imagen=pygame.image.load('animales.png').convert_alpha()
    m=sacar_pixel(imagen)
    bl=Jugador(15,20,m)

    general=pygame.sprite.Group()
    general.add(bl)

    reloj=pygame.time.Clock()

    bl.rect.x=0
    bl.rect.y=0
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    bl.var_y=-5
                    bl.dir=3
                if event.key==pygame.K_RIGHT:
                    bl.var_x=5
                    bl.dir=2
                if event.key==pygame.K_LEFT:
                    bl.var_x=-5
                    bl.dir=1
                if event.key==pygame.K_DOWN:
                    bl.var_y=5
                    bl.dir=0
            if event.type==pygame.KEYUP and (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                bl.var_x=0
            if event.type==pygame.KEYUP and (event.key==pygame.K_UP or event.key==pygame.K_DOWN):
                bl.var_y=0
        general.update()
        pantalla.fill(NEGRO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
if __name__=='__main__':main(0)
