import pygame
from time import sleep


pygame.init()
pygame.joystick.init()

joystick0 = pygame.joystick.Joystick(0)
joystick0.init()
axis0 = 0.0
axis1 = 0.0

done = False
A1="A1"
A2="A2"
print(joystick0.get_numaxes())

while done == False:
    #sleep(0.3)
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        # User did something
        if event.type == pygame.QUIT:
            done = True
            
        axis0 = joystick0.get_axis(0)
        axis1 = joystick0.get_axis(1)
        # up 0,-1 down 0,1 left -1,0 right 1,0
        if axis0 != 0.0 or axis1 != 0.0:
            print(f"{axis0}, {axis1}")
        
            

