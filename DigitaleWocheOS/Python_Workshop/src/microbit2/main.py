from microbit import *

while True:
    display.scroll(temperature())
    sleep(500)