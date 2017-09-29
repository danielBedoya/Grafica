import pygame

ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
centro=[ANCHO/2,ALTO/2]

class Bloque(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()


if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    bl=Bloque(50,70)

    general=pygame.sprite.Group()
    general.add(bl)

    reloj=pygame.time.Clock()

    bl.rect.x=100
    bl.rect.y=100
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
        bl.rect.x+=5
        bl.rect.y=100
        pantalla.fill(BLANCO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
