import pygame 
import sys

def home(screen, x1, y1, x2, y2, color):
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
    width, height=0,0
    screen= pygame.display.set_mode((width, height))
    pygame.display.set_caption("home line")
    white= (255,255,255)
    black=(0,0,0)
        
    running= True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill(black)
        home(screen, 100 ,50 ,150 ,100 ,white)  #\
        home(screen, 100 ,50 ,50 ,100 ,white)   #/
        home(screen, 50 ,100 ,150 ,100 ,white)  #-
        home(screen, 50 ,100 ,50 ,200 ,white)   #|
        home(screen, 150 ,100 ,150 ,200 ,white) #|
        home(screen, 50 ,200 ,150 ,200 ,white)  #_
        home(screen, 75 ,150 ,75 ,200 ,white)   #|
        home(screen, 75 ,150 ,125 ,150 ,white)  #-
        home(screen, 125 ,150 ,125 ,200 ,white) #|
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ =="__main__":
    main()
