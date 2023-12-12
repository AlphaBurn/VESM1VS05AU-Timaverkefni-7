from machine import Pin, PWM
from time import sleep_ms
from random import randint
import machine, neopixel
import machine

takki1 = Pin(11, Pin.IN, Pin.PULL_UP)
takki2 = Pin(10, Pin.IN, Pin.PULL_UP)
takki3 = Pin(6, Pin.IN, Pin.PULL_UP)
takki4 = Pin(46, Pin.IN, Pin.PULL_UP)
takki_led1 = Pin(3, Pin.OUT)
takki_led2 = Pin(8, Pin.OUT)
takki_led3 = Pin(18, Pin.OUT)
takki_led4 = Pin(17, Pin.OUT)

hatalari = PWM(Pin(14), freq=10000)

teningur_ledA = Pin(35, Pin.OUT)
teningur_ledB = Pin(48, Pin.OUT)
teningur_ledC = Pin(47, Pin.OUT)
teningur_ledD = Pin(45, Pin.OUT)
teningur_ledE = Pin(36, Pin.OUT)
teningur_ledF = Pin(0, Pin.OUT)
teningur_ledG = Pin(21, Pin.OUT)

greenled1 = Pin(16, Pin.OUT)
greenled2 = Pin(15, Pin.OUT)
greenled3 = Pin(7, Pin.OUT)

redled1 = Pin(6, Pin.OUT)
redled2 = Pin(5, Pin.OUT)
redled3 = Pin(4, Pin.OUT)

blueled1 = Pin(37, Pin.OUT)
blueled2 = Pin(38, Pin.OUT)
blueled3 = Pin(39, Pin.OUT)

yellowled1 = Pin(40, Pin.OUT)
yellowled2 = Pin(41, Pin.OUT)
yellowled3 = Pin(42, Pin.OUT)

p1koth = 0
p2koth = 0
p3koth = 0
p4koth = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
none = (0,0,0)

neo = neopixel.NeoPixel(machine.Pin(12), 8)

reed_switch = Pin(13, Pin.IN, Pin.PULL_UP)

notes = {'C4': 261, 'D4': 293, 'E4': 329, 'F4': 349, 'G4': 392, 'A4': 440, 'B4': 493}

def play_note(note, duration_ms):
    hatalari.freq(notes[note])
    hatalari.duty(4)
    sleep_ms(duration_ms)
    hatalari.duty(0)

simple_tune = [
    ('C4', 850), ('D4', 850), ('E4', 850), ('F4', 850),
    ('G4', 850), ('A4', 850), ('B4', 850), ('C4', 850),
    ('D4', 850), ('E4', 850), ('F4', 850), ('G4', 850),
    ('A4', 850), ('B4', 850), ('C4', 850), ('D4', 850),
    ('C4', 700), ('D4', 700), ('E4', 700), ('F4', 700),
    ('G4', 700), ('A4', 700), ('B4', 700), ('C4', 700),
    ('D4', 700), ('E4', 700), ('F4', 700), ('G4', 700),
    ('A4', 700), ('B4', 700), ('C4', 700), ('D4', 700),
    ('C4', 550), ('D4', 550), ('E4', 550), ('F4', 550),
    ('G4', 550), ('A4', 550), ('B4', 550), ('C4', 550),
    ('D4', 550), ('E4', 550), ('F4', 550), ('G4', 550),
    ('A4', 550), ('B4', 550), ('C4', 550), ('D4', 550),
    ('C4', 400), ('D4', 400), ('E4', 400), ('F4', 400),
    ('G4', 400), ('A4', 400), ('B4', 400), ('C4', 400),
    ('D4', 400), ('E4', 400), ('F4', 400), ('G4', 400),
    ('A4', 400), ('B4', 400), ('C4', 400), ('D4', 400),
    ('C4', 250), ('D4', 250), ('E4', 250), ('F4', 250),
    ('G4', 250), ('A4', 250), ('B4', 250), ('C4', 250),
    ('D4', 250), ('E4', 250), ('F4', 250), ('G4', 250),
    ('A4', 250), ('B4', 250), ('C4', 250), ('D4', 250),
    ('C4', 100), ('D4', 100), ('E4', 100), ('F4', 100),
    ('G4', 100), ('A4', 100), ('B4', 100), ('C4', 100),
    ('D4', 100), ('E4', 100), ('F4', 100), ('G4', 100),
    ('A4', 100), ('B4', 100), ('C4', 100), ('D4', 100),
    ('C4', 50), ('D4', 50), ('E4', 50), ('F4', 50),
    ('G4', 50), ('A4', 50), ('B4', 50), ('C4', 50),
    ('D4', 50), ('E4', 50), ('F4', 50), ('G4', 50),
    ('A4', 50), ('B4', 50), ('C4', 50), ('D4', 50)
]

victory_tune = [
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

def rgb(pix1, pix2, pix3, pix4, pix5, pix6, pix7, pix8):
    neo[0] = pix1
    neo[1] = pix2
    neo[2] = pix3
    neo[3] = pix4
    neo[4] = pix5
    neo[5] = pix6
    neo[6] = pix7
    neo[7] = pix8
    neo.write()

def teningar_Slokkva():
    teningur_ledA.value(0)
    teningur_ledB.value(0)
    teningur_ledC.value(0)
    teningur_ledD.value(0)
    teningur_ledE.value(0)
    teningur_ledF.value(0)
    teningur_ledG.value(0)

def teningur1():
    teningar_Slokkva()
    teningur_ledG.value(1)

def teningur2():
    teningar_Slokkva()
    teningur_ledA.value(1)
    teningur_ledB.value(1)
    
def teningur3():
    teningar_Slokkva()
    teningur_ledB.value(1)
    teningur_ledG.value(1)
    teningur_ledE.value(1)

def teningur4():
    teningar_Slokkva()
    teningur_ledA.value(1)
    teningur_ledB.value(1)
    teningur_ledE.value(1)
    teningur_ledF.value(1)

def teningur5():
    teningar_Slokkva()
    teningur_ledA.value(1)
    teningur_ledB.value(1)
    teningur_ledG.value(1)
    teningur_ledE.value(1)
    teningur_ledF.value(1)

def teningur6():
    teningar_Slokkva()
    teningur_ledA.value(1)
    teningur_ledB.value(1)
    teningur_ledC.value(1)
    teningur_ledD.value(1)
    teningur_ledE.value(1)
    teningur_ledF.value(1)
    
def showall():
    teningar_Slokkva()
    teningur_ledA.value(1)
    teningur_ledB.value(1)
    teningur_ledC.value(1)
    teningur_ledD.value(1)
    teningur_ledE.value(1)
    teningur_ledF.value(1)
    teningur_ledG.value(1)

def syna_tening(tala):
    if tala == 1:
        teningur1()
    elif tala == 2:
        teningur2()
    elif tala == 3:
        teningur3()
    elif tala == 4:
        teningur4()
    elif tala == 5:
        teningur5()
    elif tala == 6:
        teningur6()

def takkaled(led1, led2, led3, led4):
    takki_led1.value(led1)
    takki_led2.value(led2)
    takki_led3.value(led3)
    takki_led4.value(led4)
    
def slokkvaLed():
    redled1.value(0)
    redled2.value(0)
    redled3.value(0)
    blueled1.value(0)
    blueled2.value(0)
    blueled3.value(0)
    greenled1.value(0)
    greenled2.value(0)
    greenled3.value(0)
    yellowled1.value(0)
    yellowled2.value(0)
    yellowled3.value(0)
    
byrjun = True
testing = 33
byrjar = randint(1,4)
reed_breyta = 0

while True:
    if byrjar == 1:
        print("Player: 1")
        teningar_Slokkva()
        takkaled(1, 0, 0, 0)
        if takki1.value() == 0 or testing == 33:
            syna_tening(randint(1,6))
            print("Kastad")
            for i in simple_tune:
                if takki1.value() == 0:
                    break
                elif reed_switch.value() == 0 and reed_breyta == 1:
                    rgb(red, red, red, red, red, red, red, red)
                elif reed_switch.value() == 1:
                    rgb(none, none, none, none, none, none, none, none)
                    neo.write()
                    p1koth = 0
                    p2koth = 0
                    p3koth = 0
                    p4koth = 0
                    slokkvaLed()
                    reed_breyta = 1
                play_note(*i)
                sleep_ms(20)
            if reed_switch.value() == 0 and reed_breyta == 1:
                print("KOTH: RED")
                rgb(red, red, red, red, red, red, red, red)
                p1koth += 1
            byrjar +=1
            if p1koth == 1:
                redled1.value(1)
            elif p1koth == 2:
                redled2.value(1)
            elif p1koth == 3:
                redled3.value(1)
                sleep_ms(1000)
                teljari = 0
                for i in victory_tune:
                    play_note(*i)
                    if teljari % 2 == 0:
                        takkaled(1, 0, 0, 0)
                        redled1.value(1)
                        redled2.value(1)
                        redled3.value(1)
                    else:
                        takkaled(0, 0, 0, 0)
                        redled1.value(0)
                        redled2.value(0)
                        redled3.value(0)
                    teljari += 1
                sleep_ms(1000)
                exit()
            else:
                redled1.value(0)
                redled2.value(0)
                redled3.value(0)

        continue
    
    elif byrjar == 2:
        print("Player: 2")
        teningar_Slokkva()
        takkaled(0, 1, 0, 0)
        if takki2.value() == 0 or testing == 33:
            syna_tening(randint(1,6))
            print("Kastad")
            for i in simple_tune:
                if takki2.value() == 0:
                    break
                elif reed_switch.value() == 0 and reed_breyta == 2:
                    rgb(blue, blue, blue, blue, blue, blue, blue, blue)
                elif reed_switch.value() == 1:
                    rgb(none, none, none, none, none, none, none, none)
                    neo.write()
                    p1koth = 0
                    p2koth = 0
                    p3koth = 0
                    p4koth = 0
                    slokkvaLed()
                    reed_breyta = 2
                play_note(*i)
                sleep_ms(20)
            if reed_switch.value() == 0 and reed_breyta == 2:
                print("KOTH: BLUE")
                rgb(blue, blue, blue, blue, blue, blue, blue, blue)
                p2koth += 1
            byrjar +=1
            if p2koth == 1:
                blueled1.value(1)
            elif p2koth == 2:
                blueled2.value(1)
            elif p2koth == 3:
                blueled3.value(1)
                sleep_ms(1000)
                teljari = 0
                for i in victory_tune:
                    play_note(*i)
                    if teljari % 2 == 0:
                        takkaled(0, 1, 0, 0)
                        blueled1.value(1)
                        blueled2.value(1)
                        blueled3.value(1)
                    else:
                        takkaled(0, 0, 0, 0)
                        blueled1.value(0)
                        blueled2.value(0)
                        blueled3.value(0)
                    teljari += 1
                sleep_ms(1000)
                exit()
            else:
                blueled1.value(0)
                blueled2.value(0)
                blueled3.value(0)
        continue
    elif byrjar == 3:
        print("Player: 3")
        teningar_Slokkva()
        takkaled(0, 0, 1, 0)
        if takki3.value() == 0 or testing == 33:
            syna_tening(randint(1,6))
            print("Kastad")
            for i in simple_tune:
                if takki3.value() == 0:
                    break
                elif reed_switch.value() == 0 and reed_breyta == 3:
                    rgb(green, green, green, green, green, green, green, green)
                elif reed_switch.value() == 1:
                    rgb(none, none, none, none, none, none, none, none)
                    neo.write()
                    p1koth = 0
                    p2koth = 0
                    p3koth = 0
                    p4koth = 0
                    slokkvaLed()
                    reed_breyta = 3
                play_note(*i)
                sleep_ms(20)
            if reed_switch.value() == 0 and reed_breyta == 3:
                print("KOTH: GREEN")
                rgb(green, green, green, green, green, green, green, green)
                p3koth += 1
            byrjar +=1
            if p3koth == 1:
                greenled1.value(1)
            elif p3koth == 2:
                greenled2.value(1)
            elif p3koth == 3:
                greenled3.value(1)
                sleep_ms(1000)
                teljari = 0
                for i in victory_tune:
                    play_note(*i)
                    if teljari % 2 == 0:
                        takkaled(0, 0, 1, 0)
                        greenled1.value(1)
                        greenled2.value(1)
                        greenled3.value(1)
                    else:
                        takkaled(0, 0, 0, 0)
                        greenled1.value(0)
                        greenled2.value(0)
                        greenled3.value(0)
                    teljari += 1
                sleep_ms(1000)
                exit()
            else:
                greenled1.value(0)
                greenled2.value(0)
                greenled3.value(0)
        continue
    elif byrjar == 4:
        print("Player: 4")
        teningar_Slokkva()
        takkaled(0, 0, 0, 1)
        if takki4.value() == 0 or testing == 33:
            syna_tening(randint(1,6))
            print("Kastad")
            for i in simple_tune:
                if takki4.value() == 0:
                    break
                elif reed_switch.value() == 0 and reed_breyta == 4:
                    rgb(yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow)
                elif reed_switch.value() == 1:
                    rgb(none, none, none, none, none, none, none, none)
                    neo.write()
                    p1koth = 0
                    p2koth = 0
                    p3koth = 0
                    p4koth = 0
                    slokkvaLed()
                    reed_breyta = 4
                play_note(*i)
                sleep_ms(20)
            if reed_switch.value() == 0 and reed_breyta == 4:
                print("KOTH: YELLOW")
                rgb(yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow)
                p4koth += 1
            byrjar = 1
            if p4koth == 1:
                yellowled1.value(1)
            elif p4koth == 2:
                yellowled2.value(1)
            elif p4koth == 3:
                yellowled3.value(1)
                sleep_ms(1000)
                teljari = 0
                for i in victory_tune:
                    play_note(*i)
                    if teljari % 2 == 0:
                        takkaled(0, 0, 0, 1)
                        yellowled1.value(1)
                        yellowblueled2.value(1)
                        yellowblueled3.value(1)
                    else:
                        takkaled(0, 0, 0, 0)
                        yellowled1.value(0)
                        yellowled2.value(0)
                        yellowled3.value(0)
                    teljari += 1
                sleep_ms(1000)
                exit()
            else:
                yellowled1.value(0)
                yellowled2.value(0)
                yellowled3.value(0)
        continue
