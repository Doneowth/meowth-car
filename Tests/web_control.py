import RPi.GPIO as gpio
import pygame
from time import sleep

FL_MOTOR = 0
FR_MOTOR = 0
RL_MOTOR = 0
RR_MOTOR = 0


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


print("motors activated")
run = True
pygame.init()
size = [500, 900]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Keyboard Controller")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYUP:
            gpio.cleanup()
        # keys control
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("finished")
                gpio.cleanup()
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()
            if event.key == pygame.K_UP:
                forward()
            if event.key == pygame.K_DOWN:
                backward()
            else:
                gpio.cleanup()


