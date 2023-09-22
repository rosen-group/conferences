from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll(microphone.sound_level())
        sleep(200)
    else:
        display.clear()
