import os
import platform
import subprocess
import threading
import tkinter as tk


def run_build(output_text, close_button):
    output_text.insert(tk.END, "[+] Exécution de build.py...\n")
    close_button.config(state=tk.DISABLED)  # Désactiver le bouton "Fermer"

    process = subprocess.Popen(['python3', 'build.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               universal_newlines=True)
    for line in process.stdout:
        output_text.insert(tk.END, line)
        output_text.see(tk.END)
    process.stdout.close()

    return_code = process.wait()
    if return_code == 0:
        output_text.insert(tk.END, "[+] build.py terminé.\n")
    else:
        output_text.insert(tk.END, "[X] Erreur lors de l'exécution de build.py.\n")

    close_button.config(state=tk.NORMAL)  # Réactiver le bouton "Fermer"


def close_window(window):
    window.destroy()


def run_build_button(output_text, close_button):
    build_thread = threading.Thread(target=run_build, args=(output_text, close_button))
    build_thread.start()


def create_window():
    if os.name == 'posix':
        window = tk.Tk()
        window.title("Exécution de build.py")
        window.geometry("800x600")

        output_text = tk.Text(window, width=80, height=27)
        output_text.pack(pady=10)

        close_button = tk.Button(window, text="Fermer", command=lambda: close_window(window))
        close_button.pack(pady=5)

        build_button = tk.Button(window, text="Configuration",
                                 command=lambda: run_build_button(output_text, close_button))
        build_button.pack(pady=5)

        window.mainloop()


def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


number = '1'
data = ""

# def check_install_xterm():
#     try:
#         subprocess.run(['xterm', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     except FileNotFoundError:
#         print("[!] xterm n'est pas installé sur votre système.")
#         install_xterm = input("Voulez-vous installer xterm maintenant ? (y/n): ")
#         if install_xterm.lower() == 'y':
#             try:
#                 subprocess.run(['sudo', 'apt-get', 'install', '-y', 'xterm'], check=True)
#                 print("[+] xterm a été installé avec succès.")
#             except subprocess.CalledProcessError:
#                 print("[X] Erreur lors de l'installation de xterm.")
#                 sys.exit(1)
#         else:
#             print("[X] xterm est nécessaire pour exécuter ce programme. Veuillez l'installer et réessayer.")
#             sys.exit(1)
#
# check_install_xterm()
#
# subprocess.run(['sudo', 'pip', 'install', 'tinydb'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#
# os.environ['TERM'] = 'xterm'
# path = os.getcwd()

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
