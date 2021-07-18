import RPi.GPIO as gpio
import pygame
from time import sleep

FL_MOTOR = 0
FR_MOTOR = 0
RL_MOTOR = 0
RR_MOTOR = 0


def forward():
    init()
    gpio.output(17, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)    
    #sleep(sleep_time)
    #gpio.cleanup()

def left():
    init()
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)    
    #sleep(t)
    #gpio.cleanup()

def right():
    init()
    gpio.output(17, gpio.HIGH)    
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.HIGH)
    #sleep(t)
    #gpio.cleanup()

#lhlh
def backward():
    
    init()
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.HIGH)  
    #sleep(sleep_time)
    #gpio.cleanup()


def init():
    gpio.setwarnings(False)
    #gpio.cleanup()
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

#gpio.cleanup()


print("motors activated")
run = True
pygame.init()
pygame.joystick.init()
joystick0 = pygame.joystick.Joystick(0)
joystick0.init()
size = [500, 900]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My PS4 JoyStck Controller")
while run:
    #sleep(0.3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #elif event.type == pygame.KEYUP:
            gpio.cleanup()
        #elif event.type == pygame.KEYDOWN:
         #   if event.key == pygame.K_a:
          #      print("finished")
           #     gpio.cleanup() 
            #if event.key == pygame.K_LEFT:
             #   left(0.3)
           # if event.key == pygame.K_RIGHT:
            #    right(0.3)
            #if event.key == pygame.K_UP:
             #   forward(0.3)
            #if event.key == pygame.K_DOWN:
               # backward(0.3)
        axis0 = joystick0.get_axis(0)
        axis1 = joystick0.get_axis(1)
        # up 0,-1 down 0,1 left -1,0 right 1,0
        if abs(axis0) < 0.2 and axis1 < -0.6:
            forward()
        elif abs(axis0) < 0.2 and axis1 > 0.6:
            backward()
        elif abs(axis1) < 0.2 and axis0 < -0.6:
            left()
        elif abs(axis1) < 0.2 and axis0 > 0.6:
            right()
        elif abs(axis0) < 0.2 and abs(axis1) < 0.2:
            gpio.cleanup()

