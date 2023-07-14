#!/bin/bash

current_directory=$(dirname "$0")
menu_py_path="$current_directory/services/menu.py"

if [[ -f "$menu_py_path" ]]; then
  cd "$current_directory/services" || exit 1
#  gnome-terminal -- /bin/bash -c "pip3 install -r requirements.txt; read -s -n 1 -p 'Appuyez sur une touche pour continuer...';" &
  chmod +x menu.py
  sudo /usr/bin/python3 menu.py
else
  echo "Le fichier menu.py n'a pas été trouvé dans le répertoire services."
fi

