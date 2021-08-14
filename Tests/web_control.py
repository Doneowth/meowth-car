import RPi.GPIO as gpio
import pygame
from time import sleep

FL_MOTOR = 0
FR_MOTOR = 1
RL_MOTOR = 2
RR_MOTOR = 3
# 17-Low 13 backwards
# 17-High 13 forwards
# 22-Low 13 backwards 24 forwards
# 22-High 13 backwards
# 23-Low 13 backwards
# 23-High Broken
# 24-Low Broken
# 24-High OK

def forward():
    init()
    print('--forward--')
    gpio.output(17, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)    


def left():
    init()
    print('--left--')
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)    


def right():
    init()
    print('--right--')
    gpio.output(17, gpio.HIGH)    
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.HIGH)


def backward():
    init()
    print('--backward--')
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.HIGH)  


def init():
    gpio.setwarnings(False)

    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    
def clean_up_gpio():
    gpio.cleanup()


print("motors activated")
run = True
pygame.init()
size = [200, 200]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Keyboard Controller")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("quit")
            exit(0)
        elif event.type == pygame.KEYUP:
            gpio.cleanup()
        # keys control
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("finished")
                gpio.cleanup()
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
                gpio.cleanup()
        else:
            gpio.cleanup()
