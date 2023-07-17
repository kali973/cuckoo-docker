import os
import platform
import subprocess
import threading

try:
    import tkinter as tk
except ImportError:
    print("[!] Le module 'tkinter' n'est pas installé sur votre système. Installation en cours...")
    try:
        if platform.system() == 'Linux':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3-tk'])
        elif platform.system() == 'Darwin':
            subprocess.run(['brew', 'install', 'python-tk'])
        elif platform.system() == 'Windows':
            print("[!] Veuillez installer 'tkinter' à partir du site officiel Python.")
        import tkinter as tk
        print("[+] 'tkinter' a été installé avec succès.")
    except subprocess.CalledProcessError:
        print("[X] Erreur lors de l'installation de 'tkinter'. Veuillez l'installer manuellement.")
        quit()


def run_build(output_text, close_button):
    output_text.insert(tk.END, "[+] Configuration ...\n")
    close_button.config(state=tk.DISABLED)  # Désactiver le bouton "Fermer"

    process = subprocess.Popen(['python3', 'build.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               universal_newlines=True)
    for line in process.stdout:
        output_text.insert(tk.END, line)
        output_text.see(tk.END)
    process.stdout.close()

    return_code = process.wait()
    if return_code == 0:
        output_text.insert(tk.END, "[+] configuration terminé.\n")
    else:
        output_text.insert(tk.END, "[X] Erreur lors de l'exécution de build.py.\n")

    close_button.config(state=tk.NORMAL)  # Réactiver le bouton "Fermer"


def close_window(window):
    window.destroy()


def run_build_button(output_text, close_button):
    build_thread = threading.Thread(target=run_build, args=(output_text, close_button))
    build_thread.start()


def create_window():
    window = tk.Tk()
    window.title("Configuration")
    window.geometry("800x600")

    output_text = tk.Text(window, width=80, height=27)
    output_text.pack(pady=10)

    close_button = tk.Button(window, text="  Fermer  ", command=lambda: close_window(window))
    close_button.pack(pady=5)

    build_button = tk.Button(window, text="Exécution",
                             command=lambda: run_build_button(output_text, close_button))
    build_button.pack(pady=5)

    window.mainloop()


def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


number = '1'
data = ""

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
        create_window()
        print("\033[H\033[J", end="")
        print("\033[H\033[J", end="")
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        clear()
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2 or 0\n")
