import sys
import pygame
import pygame.camera
from car_control import *

pygame.init()
pygame.camera.init()
pygame.display.set_caption('meowth-car-remote-center')

screen = pygame.display.set_mode((640,480))
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0],(640,480))
cam.start()
my_font = pygame.font.SysFont('Arial', 40)
running = True
clock = pygame.time.Clock()
while running:
    live_img = pygame.transform.rotate(cam.get_image(), 0)
    live_img = pygame.transform.scale(live_img,(640,480))
    screen.blit(live_img,(0,0))
    fps_overlay = my_font.render(
        'fps: '+ (str(clock.get_fps())),
        1, pygame.Color(0,255,0))
    screen.blit(fps_overlay, (450,5))
    pygame.display.update()
    clock.tick(60)
    
    #print("pre time: " + str(pygame.time.Clock().get_fps()))
    for event in pygame.event.get():
        # keys control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("finished")
                clean_up_gpio()
            elif event.key == pygame.K_LEFT:
                print("==left==")
                left()
            elif event.key == pygame.K_RIGHT:
                print("==right==")                
                right()
            elif event.key == pygame.K_UP:
                print("==forward==") 
                forward()
            elif event.key == pygame.K_DOWN:
                print("==backward==")
                backward()
            else:
                clean_up_gpio()
        elif event.type == pygame.KEYUP:
            gpio.cleanup()
        elif event.type == pygame.QUIT:
            running = False
            cam.stop()
            pygame.quit()
            
            exit(0)
