
import pygame
import random
pygame.init()



win=pygame.display.set_mode((500,500))
win.fill((255,255,255))
pygame.display.update()
pygame.display.set_caption("circle")

rad=10
left_held=False
pos1=None
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
        
            
        pos=pygame.mouse.get_pos()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                left_held=True
                pygame.draw.circle(win,color,pos,rad)
                if pos1:
                    pygame.draw.line(win,(0,0,0),pos,pos1,2)
                pygame.display.update()
                pos1=pos
               

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_held = False
                rad=10
                
        
       

        

        
           

       

    if left_held:
        rad+=.1
        
        pygame.draw.circle(win,color,pos,rad)
        pygame.display.update()
        

    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==3 and pos1:
            pygame.draw.circle(win,(255,255,255),pos1,rad)
            pygame.draw.line(win,(255,255,255),pos1,pos,2)
            pygame.display.update()   
                

    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        win.fill((255,255,255))
        pygame.display.update()
    if keys[pygame.K_s]:
        pygame.image.save(win, "C:\Users\user\OneDrive\Desktop\circle.png")
        print("saved")
                

   
    
   
                
                
            


    