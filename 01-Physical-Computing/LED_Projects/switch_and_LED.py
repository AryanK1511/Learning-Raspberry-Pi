from gpiozero import LED, Button
from time import sleep

# Log that the program is running
print("Program is Running")

# Initiialize the components and the pins
led = LED(25)
button = Button(2)

# Execute some logic when the button is pressed
button.wait_for_press()
led.on()
sleep(5)
led.off()
