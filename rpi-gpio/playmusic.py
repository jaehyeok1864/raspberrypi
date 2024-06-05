from time import sleep
from gpiozero import Button
from gpiozero import PWMOutputDevice

button_pin = 24
buzzer_pin = 12
music_on = True

button = Button(button_pin, pull_up=False)

def button_pressed():
    global music_on
    music_on = not music_on
    print(f"Button Pressed! Music_On = {music_on}")

button.when_pressed = button_pressed

tones = [262, 294, 330, 349, 392, 440, 494, 523]
music = [4, 4, 5, 5, 4, 4, 2, 4, 4, 2, 2, 1]
term = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1]

def play_music(buzzer_pin):
    pwm_device = PWMOutputDevice(pin=buzzer_pin, frequency=100, initial_value=0.5)
    
    try:
        while True:
            while not music_on:
                pass
            print("\nMusic on !!")
            for i in range(len(music)):
                if not music_on:
                    print("\nMusic off !!")
                    break
                pwm_device.frequency = tones[music[i]]
                pwm_device.value = 0.5
                sleep(term[i])
                pwm_device.value = 0
    finally:
        pwm_device.close()
        print("I'm Done!!")

play_music(buzzer_pin)
