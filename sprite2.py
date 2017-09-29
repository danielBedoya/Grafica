import pygame
import random

ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
AZUL=(59,131,189)
centro=[ANCHO/2,ALTO/2]

class Jugador(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=-5
        if self.rect.x<=0:
            self.var_x=5
        if self.rect.y>=ALTO-self.rect[3]:
            self.var_y=-5
        if self.rect.y<=0:
            self.var_y=5

class Rival(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.var_x=5
        self.var_y=5
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=-5
        if self.rect.x<=0:
            self.var_x=5
        if self.rect.y>=ALTO-self.rect[3]:
            self.var_y=-5
        if self.rect.y<=0:
            self.var_y=5



if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    bl=Jugador(50,70)

    general=pygame.sprite.Group()
    general.add(bl)

    reloj=pygame.time.Clock()

    bl.rect.x=100
    bl.rect.y=100
    rivales=pygame.sprite.Group()
    for i in range(10):
        r=Rival(20,20)
        r.rect.x=random.randrange(10, ANCHO-20)
        r.rect.y=random.randrange(10, ANCHO-20)
        rivales.add(r)
        general.add(r)
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    bl.var_x=5
                if event.key==pygame.K_LEFT:
                    bl.var_x=-5
                if event.key==pygame.K_UP:
                    bl.var_y=-5
                if event.key==pygame.K_DOWN:
                    bl.var_y=5
                if event.key==pygame.K_SPACE:
                    bl.var_x=0
                    bl.var_y=0
            if event.type==pygame.KEYUP:
                bl.var_x=0
                bl.var_y=0

        bl.update()
        pantalla.fill(BLANCO)
        rivales.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
