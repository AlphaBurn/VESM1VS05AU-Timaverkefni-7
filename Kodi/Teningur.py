from machine import Pin, PWM
from time import sleep_ms
from random import randint

takki_A = Pin(18, Pin.IN, Pin.PULL_UP)
takki_B = Pin(7, Pin.IN, Pin.PULL_UP)
takki_C = Pin(8, Pin.IN, Pin.PULL_UP)
takki_D = Pin(10, Pin.IN, Pin.PULL_UP)

teningur_ledA = Pin(38, Pin.OUT)
teningur_ledB = Pin(17, Pin.OUT)
teningur_ledC = Pin(39, Pin.OUT)
teningur_ledD = Pin(16, Pin.OUT)
teningur_ledE = Pin(35, Pin.OUT)
teningur_ledF = Pin(15, Pin.OUT)
teningur_ledG = Pin(37, Pin.OUT)

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

def teningar_Slokkva():
    teningur_ledA.value(0)
    teningur_ledB.value(0)
    teningur_ledC.value(0)
    teningur_ledD.value(0)
    teningur_ledE.value(0)
    teningur_ledF.value(0)
    teningur_ledG.value(0)
    
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
    
            

byrjun = True

while True:
    
    
    if takki_A.value() == 0:
        tala = randint(1,6)
        print("takki")
        syna_tening(tala)
        sleep_ms(100)
        
     
    if takki_B.value() == 0:
        tala = randint(1,6)
        print("takki")
        syna_tening(tala)
        sleep_ms(100)
    
     
    if takki_C.value() == 0:
        tala = randint(1,6)
        print("takki")
        syna_tening(tala)
        sleep_ms(100)
    
     
    if takki_D.value() == 0:
        tala = randint(1,6)
        print("takki")
        syna_tening(tala)
        sleep_ms(100)
        
        
        
    
        
        
        







