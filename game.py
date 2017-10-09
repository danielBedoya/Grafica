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
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.vidas=5
        self.var_x=0
        self.var_y=0
        self.record=0
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

class Live(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('heart_opt.jpg')
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=5

    def update(self):
        self.rect.y+=self.var_y

class Rival(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
        self.temporizador=random.randrange(800)
    def update(self):
        if self.temporizador>0:
            self.temporizador -=1
        else:
            self.rect.y+=self.var_y
        
    def gen_rivales(self,general,rivales):
        r=Rival(20,20)
        r.rect.x=random.randrange(10, ANCHO-20)
        r.rect.y=-20
        rivales.add(r)
        general.add(r)

class Proyectil(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('bala_opt.png')
        self.rect=self.image.get_rect()
        self.var_y=-5

    def update(self):
        self.rect.y+=self.var_y

def game_over(pantalla,recordper):
    pantalla.fill(NEGRO)
    image=pygame.image.load('stop_opt.png')
    pantalla.blit(image,[180,50])
    fuenteBásica = pygame.font.SysFont(None, 30)
    texto = fuenteBásica.render('Juego Terminado', True, BLANCO)
    texto1 = fuenteBásica.render('Presione 1 para reiniciar', True, BLANCO)
    texto2 = fuenteBásica.render('Presione 2 para salir', True, BLANCO)
    textRect = texto.get_rect()
    textRect.centerx = pantalla.get_rect().centerx
    textRect.centery = pantalla.get_rect().centery
    pantalla.blit(texto, [textRect[0]-50,textRect[1]-90])
    pantalla.blit(texto1, [textRect[0]-50,textRect[1]-60])
    pantalla.blit(texto2, [textRect[0]-50,textRect[1]-40])
    pygame.display.update()
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    main(recordper)
                if event.key==pygame.K_2:
                    sys.exit()

def print_extras(pantalla,vidas,record,bl_record):
    heart=pygame.image.load('heart_opt.jpg')
    x=0
    for i in range(vidas):
        pantalla.blit(heart,[0+x,380])
        x+=50
    fuenteBásica = pygame.font.SysFont(None, 20)
    texto = fuenteBásica.render('Su record es: '+str(record), True, NEGRO)
    pantalla.blit(texto, [450,0])
    texto1 = fuenteBásica.render('Su puntaje actual es: '+str(bl_record), True, NEGRO)
    pantalla.blit(texto1, [440,25])
def pausa(pantalla,reloj,recordper):
    pantalla.fill(NEGRO)
    image=pygame.image.load('pause_opt.png')
    pantalla.blit(image,[180,50])
    fuenteBásica = pygame.font.SysFont(None, 30)
    texto = fuenteBásica.render('Menu de pausa', True, BLANCO)
    texto1 = fuenteBásica.render('Presione 1 o p para continuar', True, BLANCO)
    texto2 = fuenteBásica.render('Presione 2 para reiniciar', True, BLANCO)
    texto3 = fuenteBásica.render('Presione 3 para salir', True, BLANCO)
    textRect = texto.get_rect()
    textRect.centery = pantalla.get_rect().centery
    textRect.centerx = pantalla.get_rect().centerx
    pantalla.blit(texto, [textRect[0]-50,textRect[1]-90])
    pantalla.blit(texto1, [textRect[0]-50,textRect[1]-60])
    pantalla.blit(texto2, [textRect[0]-50,textRect[1]-40])
    pantalla.blit(texto3, [textRect[0]-50,textRect[1]-20])
    pygame.display.update()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1 or event.key==pygame.K_p:
                    return
                if event.key==pygame.K_2:
                    main(recordper)
                if event.key==pygame.K_3:
                    sys.exit()
        reloj.tick(60)

def main(recordper):
    pygame.init()
    pygame.display.set_caption('Cube Shoot')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    bl=Jugador(15,20)

    general=pygame.sprite.Group()
    general.add(bl)

    reloj=pygame.time.Clock()

    bl.rect.x=1
    bl.rect.y=350
    rivales=pygame.sprite.Group()
    for i in range(9):
        r=Rival(20,20)
        r.rect.x=random.randrange(10, ANCHO-20)
        r.rect.y=-1*random.randrange(25, 35)
        rivales.add(r)
        general.add(r)
    balas=pygame.sprite.Group()
    lives=pygame.sprite.Group()
    general.add(balas,lives,rivales)
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
    activador=True
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pausa(pantalla,reloj,recordper)
                if event.key==pygame.K_RIGHT and bl.rect.x<=ANCHO-bl.rect[2]:
                    bl.var_x=5
                if event.key==pygame.K_LEFT:
                    bl.var_x=-5
                if event.key==pygame.K_SPACE:
                    b=Proyectil()
                    b.rect.x=bl.rect.x+(bl.rect[2]/2)-7
                    b.rect.y=(bl.rect.y)
                    balas.add(b)
                    general.add(b)
            if event.type==pygame.KEYUP and (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                bl.var_x=0
        for b in balas:
            ls_col=pygame.sprite.spritecollide(b,rivales,True)
            for e in ls_col:
                rivales.remove(e)
                balas.remove(b)
                general.remove(b)
                r.gen_rivales(general,rivales)
                bl.record+=1
                activador=True
                if bl.record%20==0 and bl.record>0:
                    l=Live()
                    l.rect.x=random.randrange(10, ANCHO-20)
                    l.rect.y=-1*random.randrange(25, 35)
                    lives.add(l)
                    general.add(l)
            if b.rect.y<0:
                balas.remove(b)
                general.remove(b)
        ls_col=pygame.sprite.spritecollide(bl,rivales,True)
        if ls_col:
            for r in ls_col:
                rivales.remove(r)
                general.remove(r)
                r.gen_rivales(general,rivales)
                bl.vidas-=1
        ls_col=pygame.sprite.spritecollide(bl,lives,True)
        if ls_col:
            for l in ls_col:
                lives.remove(l)
                general.remove(l)
                if bl.vidas<=12:
                    bl.vidas+=1
        for r in rivales:
            if r.rect.y>=350:
                r.rect.y=-1*(random.randrange(random.randrange(ALTO+30,ALTO+500, 15)))
                bl.vidas-=1
            if r.rect.y<=0:
                r.var_y=1
        if bl.vidas==0:
            game_over(pantalla,recordper)
        for l in lives:
            if l.rect.y>=350:
                lives.remove(l)
                general.remove(l)
        if bl.record>recordper:
            recordper=bl.record
        if bl.record%30==0 and bl.record!=0 and activador:
            for i in range(3):
                r=Rival(20,20)
                r.rect.x=random.randrange(10, ANCHO-20)
                r.rect.y=-1*random.randrange(25, 35)
                rivales.add(r)
                general.add(r)
            activador=False

        pantalla.fill(BLANCO)
        general.update()
        general.draw(pantalla)
        pygame.draw.line(pantalla,AZUL,[0,370],[600,370],1)
        print_extras(pantalla,bl.vidas,recordper,bl.record)
        pygame.display.flip()
        reloj.tick(60)
if __name__=='__main__':main(0)