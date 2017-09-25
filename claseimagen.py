import pygame

ALTO=480
ANCHO=640
ROJO=(255,0,0)
BLANCO=(255,255,255)
centro=[ANCHO/2,ALTO/2]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    tux=pygame.image.load('tux.png')
    var=tux.get_rect()
    jup=pygame.image.load('jupiter.jpg')
    pantalla.blit(jup,[0,0])
    pygame.display.flip()
    fin=False
    y=100
    x=100
    var_y=0
    var_x=0
    reloj=pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                t=pygame.key.name(event.key)
                print(t)
                if t=='up':
                    var_y=-5
                    var_x=0
                if t=='left':
                    var_x=-5
                    var_y=0
                if t=='right':
                    var_x=5
                    var_y=0
                if t=='down':
                    var_y=5
                    var_x=0
            if event.type == pygame.QUIT :
             fin=True
        pantalla.blit(jup,[0,0])
        pantalla.blit(tux,[x,y])
        pygame.display.flip()
        y+=var_y
        x+=var_x
        if y>= ALTO-var[3]:
            y=ALTO-var[3]
            var_y=0
        if x>= ANCHO-var[2]:
            x=ANCHO-var[2]
            var_x=0
        if y<= 0:
            var_y=0
        if x<=0:
            var_x=0
        #reloj.tick(5000)
