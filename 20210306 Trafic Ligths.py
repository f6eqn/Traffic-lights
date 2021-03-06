# Projet Trafic Light
# Reprise du projet Arduino sur une plateforme Raspberry Pico
# Programmation en MicroPython
# (R) f6EQN 02/2021
#
# Importation des bibliotheques

from machine import Pin
from utime import sleep
import _thread

# initialisation de quelques variables
global i, j, k  # les index des tables de séquence


global p 
p = 0  # flag/index piéton

l = 0
k = 1  # nr de séquence de démarrage


# les tables de séquence
seq_0 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
         ]
seq_t0 = [1, 1]
        
seq_1 = [[0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
          [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 1, 0, 0, 1, 1, 0]
          ]
seq_t1 = [5, 2, 1, 5]

seq_2 = [[1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
          [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
          [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 1, 0, 0, 0, 1]
          ]
seq_t2 = [5, 2, 1, 5]

seq_n = [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         ]
seq_tn = [1, 1]

seq_p1 = [[0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
          [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
         ]
seq_tp1 = [2, 5, 2]

seq_p2 = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
          [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
          [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
          ]
seq_tp2 = [2, 5, 2]
         
         

# configuration des E/S
# liste I/O

gpio_out = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
gpio_in = [12,]

# configuration et initialisation des ports I/O

for i in gpio_out:
    Pin(i, Pin.OUT)
    pin = Pin(i)
    pin.value(0)  # RAZ sorties

global button
button = Pin(12, Pin.IN, Pin.PULL_DOWN)  # bouton d'appel piéton avec pull_down
ldr = machine.ADC(0)  # convertisseur ADC0 gpio 26

# les fonctions (affichage, détection j/n, detection bouton

def seq_n():
    global k
    j = 0
    while j <= 1:
        i = 0        
        while i <= 9:
            pin = Pin(i+2)
            pin.value(seq_0[j][i])
            i += 1
        
        sleep(seq_t0[j])  # tempo indexée
        j += 1
    
    k = 1  # prochaine sequence = j1

def seq_j1():    
    global k
    k = 2  # prochaine sequence = 2
    j = 0
    while j <= 2:
        i = 0        
        while i <= 9:
            pin = Pin(i+2)
            pin.value(seq_1[j][i])            
            i += 1
        
        sleep(seq_t1[j])  # tempo indexée
        j += 1
    
def seq_j2():    
    global k
    k = 1  # prochaine sequence = 1
    j = 0
    while j <= 2:
        i = 0        
        while i <= 9:
            pin = Pin(i+2)
            pin.value(seq_2[j][i])            
            i += 1
        
        sleep(seq_t2[j])  # tempo indexée
        j += 1


def seq_pt1():
    global p
    j = 0
    while j <= 2:
        i = 0        
        while i <= 9:
            pin = Pin(i+2)
            pin.value(seq_p1[j][i])            
            i += 1
        
        sleep(seq_tp1[j])  # tempo indexée
        j += 1
    p = 0  # prochaine sequence = 2
    print("+1")

def seq_pt2():
    global p
    j = 0
    while j <= 2:
        i = 0        
        while i <= 9:
            pin = Pin(i+2)
            pin.value(seq_p2[j][i])            
            i += 1
        
        sleep(seq_tp2[j])  # tempo indexée
        j += 1
    p = 0  # prochaine sequence = 1
    print("+2")

def det_nuit():
    global k
    conversion_factor = 3.3 / (65535)  # conversion en Volts
    reading = ldr.read_u16() * conversion_factor
    n = int(reading)
    val = [1, 0, 0]
    k = k*val[n]
    
def det_pieton(pin):
    global p
    button.irq(handler=None)  # desarmement de l'IRQ
    p = 2
    print('*')


button.irq(trigger=Pin.IRQ_RISING, handler=det_pieton)  # armement de l'IRQ
 
# boucle principale

sequence = [seq_n, seq_j1, seq_j2, seq_pt1, seq_pt2]
while True:
    det_nuit()
    button.irq(trigger=Pin.IRQ_RISING, handler=det_pieton)
    l = k + p
    print(l)
    sequence[l]()
   
    
    


    