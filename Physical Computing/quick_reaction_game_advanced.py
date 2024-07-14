from gpiozero import LED, Button
from time import sleep
from random import uniform
from signal import pause
from sys import exit

# Initializing the game
print("========== WELCOME TO THE REFLEX GAME ==========\n")
print("!!! First player to reach 3 points wins !!!! \n")

# Take inputs
p1 = input("Enter player 1's name: ")
p2 = input("Enter player 2's name: ")
print("\n")

# Initialize scores
p1_score, p2_score = 0, 0

# Function to print the scoreboard each time
def print_scoreboard(p1_score, p2_score):
    print("----- SCOREBOARD -----")
    print(f"{p1}: {p1_score}")
    print(f"{p2}: {p2_score}")
    print("\n")

# Initializing the components and the pins
green_led = LED(4)
p1_button = Button(3)
p2_button = Button(2)

print_scoreboard(p1_score, p2_score)

# Initialize lockout flag
lockout = False

def led_on():
    global lockout
    print("LED starting in 2 seconds")
    sleep(2)
    green_led.on()
    sleep(uniform(1, 5))
    green_led.off()
    lockout = False  # Reset lockout after LED cycle

def pressed(button):
    global p1_score, p2_score, lockout
    if lockout:
        return  # Exit function if lockout is active
    
    lockout = True  # Set lockout to prevent simultaneous scoring

    if button.pin.number == 3:
        p1_score += 1
    else:
        p2_score += 1
    print_scoreboard(p1_score, p2_score)
    
    if p1_score == 3:
        print(f"{p1} won the game")
        exit(0)
    elif p2_score == 3:
        print(f"{p2} won the game")
        exit(0)
    
    led_on()

led_on()
p2_button.when_pressed = pressed
p1_button.when_pressed = pressed


pause()
