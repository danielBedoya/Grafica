import pygame

ALTO=480
ANCHO=640
ROJO=(255,0,0)
BLANCO=(255,255,255)
centro=[ANCHO/2,ALTO/2]

def sacar_pixel(imagen,pos):
    ancho_img,alto_img=imagen.get_size()
    matriz=[]
    matriz = [None] * 12
    for i in range(12):
        matriz[i] = [None] * 32
    for j in range (12):
        for i in range (32):
            cuadro = (i*32,j*32, 32, 32)
            recorte=imagen.subsurface(cuadro)
            matriz[j][i]=recorte
    return matriz[pos[0]][pos[1]]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    imagen=pygame.image.load('terrenogen.png').convert()
    print 'ancho:',ancho_img,' alto: ',alto_img
    pantalla.blit(sacar_pixel(imagen,[11,10]),[0,0])
    pygame.display.flip()
    fin=False
    reloj=pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
             fin=True
        reloj.tick(60)
