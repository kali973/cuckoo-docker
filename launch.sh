#!/bin/bash

current_directory=$(dirname "$0")
menu_py_path="$current_directory/services/menu.py"

if [[ -f "$menu_py_path" ]]; then
  cd "$current_directory/services" || exit 1
  pip3 install -r requirements.txt  # Installer les dépendances
  chmod +x menu.py  # Changer les permissions pour le rendre exécutable
  sudo /usr/bin/python3 menu.py
else
  echo "Le fichier menu.py n'a pas été trouvé dans le répertoire services."
fi

