print("abdc")

from machine import Pin, PWM
import machine
from time import sleep_ms
import machine, neopixel

button1 = Pin(10, Pin.IN, Pin.PULL_UP)
button2 = Pin(11, Pin.IN, Pin.PULL_UP)
button3 = Pin(12, Pin.IN, Pin.PULL_UP)
button4 = Pin(13, Pin.IN, Pin.PULL_UP)
hatalari = PWM(Pin(14), freq=10000)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
none = (0,0,0)

neo = neopixel.NeoPixel(machine.Pin(16), 8)

reed_switch = Pin(17, Pin.IN, Pin.PULL_UP)
 
def rgb(pix1, pix2, pix3, pix4, pix5, pix6, pix7, pix8):
    neo[1] = pix1
    neo[2] = pix2
    neo[3] = pix3
    neo[4] = pix4
    neo[5] = pix5
    neo[6] = pix6
    neo[7] = pix7
    neo[8] = pix8
    neo.write()
    
notes = {'C4': 261, 'D4': 293, 'E4': 329, 'F4': 349, 'G4': 392, 'A4': 440, 'B4': 493}

def play_note(note, duration_ms):
    hatalari.freq(notes[note])
    hatalari.duty(10)
    sleep_ms(duration_ms)
    hatalari.duty(0)

sigur_lag = [ 
    ('E4', 150), ('G4', 150), ('C4', 150), ('E4', 150),
    ('G4', 150), ('C4', 150), ('E4', 150), ('G4', 150),
    ('G4', 150), ('C4', 150), ('E4', 150), ('G4', 150),
    ('F4', 150), ('A4', 150), ('C4', 150), ('E4', 150),
    ('F4', 150), ('A4', 150), ('C4', 150), ('E4', 150),
    ('D4', 150), ('F4', 150), ('A4', 150), ('C4', 150),
    ('D4', 150), ('F4', 150), ('A4', 150), ('C4', 150),
    ('E4', 150), ('G4', 150), ('C4', 150), ('E4', 150),
    ('E4', 150), ('G4', 150), ('C4', 150), ('E4', 150),
    ('C4', 1500)
]

while True:
    print("abc")
    if reed_switch.value() == 0:
        rgb(red, red, red, red, red, red, red, red)
        neo.write()
    else:
        rgb(none, none, none, none, none, none, none, none)
        neo.write()
    print(reed_switch.value())
# while True:
#     for i in sigur_lag:
#         play_note(*i)
#         sleep_ms(50)
#     rgb(red, blue, blue, red, green, blue, yellow, green)
#     neo.write()
#     sleep_ms(1300)
#     rgb(none, none, none, blue, red, red, yellow, green)
#     neo.write()
#     sleep_ms(1000)
    
