from time import sleep

from gpiozero import Button

Button = Button(24, pull_up=False)

def button_pressed():
    print("BUtton Pressed!")

button.when_pressed = button_pressed
    
try:
    i = 0
    while True:
        sleep(1)
        i = i + 1
        print(i)

except KeyboardInterrupt:
    print("I'm done!")