import pygame 
import sys

def dda(screen, x1, y1, x2, y2, color):
    dx = x2-x1
    dy= y2-y1

    if dx>dy: 
        step = dx

    else:
        step= dy

    Xinc= dx/step
    Yinc= dy/step

    X=x1
    Y=y1
    for i in range (step+1):
        
        screen.set_at((round(X), round(Y)),color)
        X= X+Xinc
        Y= Y+Yinc

def main():
    pygame.init()
    width, height=600, 600
    screen= pygame.display.set_mode((width, height))
    pygame.display.set_caption("dda line")
    white= (255,255,255)
    black=(0,0,0)
    x0, y0= 50, 100
    x1, y1= 500, 400
    running= True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill(black)
        dda(screen, x0,y0, x1, y1, white)
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ =="__main__":
    main()
