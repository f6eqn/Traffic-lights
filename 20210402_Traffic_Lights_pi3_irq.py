# Traffic Lights pi3_3
# reprise du projet traffic_lights
# avec utilisation des dictionnaires, des bibliothèques python3 et
# des boucles for
# F6EQN (R) 03/2021
#

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ios = (17, 27, 22, 16, 20, 21, 5, 6, 13, 23, 24, 25)
buzz = 18  # le buzzer
button = 4  # le bouton (ou 7?)

l = 1  # initialisation de l'index de séquence
# initialisation des E/S
for pin in ios:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # RAZ I/O
    
GPIO.setup(buzz, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
# séquence nuit
seq_n = ((0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0),
         (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
seq_tn = (1, 1)  # temporisations
# séqence jour
seq_j = ((1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1),
          (1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0),
          (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0),
          (0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0),
          (0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0),
          (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0))
seq_tj = (5, 2, 1, 5, 2, 1)
# séquence démarrage
seq_d = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
         (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
         (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
         (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
         (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
         (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
         (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
         (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
         (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
         (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0))
seq_td = (1, 1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
          0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1)
def buzzer():
    global buzz
    GPIO.output(buzz, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(buzz, GPIO.LOW)
    print('Bzz')
    
def write(pin,etat):
    if etat == 1:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)
        
    
def nuit():
    for j in range(len(seq_tn)):
        for i in range(len(ios)):
            pin = ios[i]
            etat = seq_n[j][i]
            write(pin,etat)
        sleep(seq_tn[j])
        print('*')
            
                  
def jour():
    for j in range(len(seq_tj)):
        for i in range(len(ios)):
            pin = ios[i]
            etat = seq_j[j][i]
            write(pin,etat)
        sleep(seq_tj[j])
        # print('/')
def init():
    for j in range(len(seq_td)):
        for i in range(len(ios)):
            pin = ios[i]
            etat = seq_d[j][i]
            write(pin,etat)
        sleep(seq_td[j])
        print('+')
        
def irq(pin):
    global l  # gestion interruption bouton
    print('IRQ')
    if l == 1:
        l = 0
    else:
        l = 1
        
        
# boucle principale
buzzer()
init()
buzzer()
GPIO.add_event_detect(button, GPIO.FALLING, callback=irq, bouncetime=300)
try:
    while True:
        buzzer()
        sequence = [nuit, jour]
        sequence[l]()
        # nuit()
        
except KeyboardInterrupt:
    print('Terminé')
    GPIO.cleanup()       

