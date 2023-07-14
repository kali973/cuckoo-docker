import logging
import os
import platform
import subprocess
import sys
import threading


def a():
    os.system("gnome-terminal -- sudo python build.py")

def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

logging.disable(sys.maxsize)
number = '1'  # Initialise la variable 'number' avec une valeur par défaut pour éviter une erreur lors de l'évaluation de la condition de la boucle
data = ""

os.system("sudo apt-get install -y xterm")

# Installation de tinydb sans afficher les avertissements
subprocess.run(['sudo', 'pip', 'install', 'tinydb'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

os.environ['TERM'] = 'xterm'
path = os.getcwd()

while number != '0':
    data += ' ----------------------------\n'
    if os.name == "nt":
        print(' [!] Please run the script on Linux Machine !')
        quit()
    elif os.name != "nt":
        data = (' ----------------------------\n')
        data += ' Hi ' + platform.uname()[1] + '\n'
    data += ' ----------------------------\n'
    data += ' Select option:\n'
    data += ' [1] Configuration environment\n'
    data += ' [0] Exit\n'
    print(data)
    number = input(" Number~# ")
    if number == '1':
        print("\n Configuration de l'environnement...\n")
        threading.Thread(target=a).start()
        print("\033[H\033[J", end="")
        print("\033[H\033[J", end="")
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        clear()
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2 or 0\n")
