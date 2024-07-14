from gpiozero import LED, Button
from time import sleep
from random import uniform
from os import _exit

# Take inputs
p1 = input("Enter player 1's name: ")
p2 = input("Enter player 2's name: ")

# Initializing the components and the pins
green_led = LED(4)
p1_button = Button(3)
p2_button = Button(2)

green_led.on()
sleep(uniform(5, 10))
green_led.off()

def pressed(button):
    if button.pin.number == 3:
        print(p1 + " won the game")
    else:
        print(p2 + " won the game")
    _exit(0)
    
p1_button.when_pressed = pressed
p2_button.when_pressed = pressed
