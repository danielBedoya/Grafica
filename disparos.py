import pygame
import random
#render es para agregar texto

ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AZUL=(59,131,189)
centro=[ANCHO/2,ALTO/2]

class Jugador(pygame.sprite.Sprite):
    def __init__(self,an,al):
	pygame.sprite.Sprite.__init__(self)
	self.image=pygame.Surface([an,al])
	self.image.fill(ROJO)
	self.rect=self.image.get_rect()
	self.vidas=5
        self.var_x=0
        self.var_y=0
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=0
        if self.rect.x<=0:
            self.rect.x=0
            self.var_x=0
        #if self.rect.y>=ALTO-self.rect[3]:
        #    self.var_y=-5
        #if self.rect.y<=0:
        #    self.var_y=5

class Rival(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
        self.temporizador=random.randrange(200)
    def update(self):
        if self.temporizador>0:
            self.temporizador -=1
        else:
            self.rect.y+=self.var_y
        #if self.rect.x>=ANCHO-self.rect[2]:
        #    self.var_x=-5
        #if self.rect.x<=0:
        #    self.var_x=5
        if self.rect.y>=350:
            self.rect.y=-1*(random.randrange(random.randrange(ALTO+30,ALTO+500, 15)))
        if self.rect.y<=0:
            self.var_y=1

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(NEGRO)
        self.rect=self.image.get_rect()
        self.var_y=-5

    def update(self):
        self.rect.y+=self.var_y


if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    bl=Jugador(100,20)

    general=pygame.sprite.Group()
    general.add(bl)

    reloj=pygame.time.Clock()

    bl.rect.x=1
    bl.rect.y=350
    rivales=pygame.sprite.Group()
    for i in range(8):
        r=Rival(20,20)
        r.rect.x=random.randrange(10, ANCHO-20)
        r.rect.y=-20
        rivales.add(r)
        general.add(r)
    balas=pygame.sprite.Group()
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT and bl.rect.x<=ANCHO-bl.rect[2]:
                    bl.var_x=12
                if event.key==pygame.K_LEFT:
                    bl.var_x=-12
                '''if event.key==pygame.K_UP:
                    bl.var_y=-5'''
                if event.key==pygame.K_DOWN:
                    b=Proyectil(15,15)
                    b.rect.x=bl.rect.x+(bl.rect[2]/2)-7
                    b.rect.y=(bl.rect.y)
                    balas.add(b)
                    general.add(b)
                if event.key==pygame.K_SPACE:
                    bl.var_x=0
                    bl.var_y=0
        for b in balas:
            ls_col=pygame.sprite.spritecollide(b,rivales,True)
            for e in ls_col:
                rivales.remove(e)
                balas.remove(b)
                general.remove(b)
        #ls_col1=pygame.sprite.groupcollide(balas,rivales,True,True)
        ls_col=pygame.sprite.spritecollide(bl,rivales,True)
        if ls_col:
            print(random.randrange(ALTO+30,ALTO+500, 5))
            r=Rival(20,20)
            r.rect.x=random.randrange(10, ANCHO-20)
            r.rect.y=-1*(random.randrange(random.randrange(ALTO+30,ALTO+500, 10)))
            rivales.add(r)
            general.add(r)
	    bl.vidas-=1
        pantalla.fill(BLANCO)
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
