import os


def update_packages():
    # Mise à jour de pip, setuptools et virtualenv
    os.system('sudo pip install --upgrade pip')
    os.system('sudo pip install --upgrade setuptools')
    os.system('sudo pip install --upgrade virtualenv')


def install_docker():
    # Mise à jour des paquets existants
    os.system('sudo apt update')

    # Installation des dépendances requises
    os.system('sudo apt install -y apt-transport-https ca-certificates curl software-properties-common')

    # Ajout de la clé GPG officielle de Docker
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor --yes -o /usr/share/keyrings/docker-archive-keyring.gpg')

    # Ajout du référentiel Docker dans les sources de paquets APT
    os.system('echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list')

    # Mise à jour des paquets APT
    os.system('sudo apt update')

    # Installation de Docker
    os.system('sudo apt install -y docker-ce docker-ce-cli containerd.io')

    # Installation des autres packages
    os.system('sudo apt install -y python3-pip')
    packages = ['pillow==3.2', 'dpkt', 'httpreplay', 'peepdf', 'pefile2', 'roach', 'yara-python']
    for package in packages:
        os.system(f'sudo pip3 install {package}')


def install_docker_compose():
    # Téléchargement de la version stable de Docker Compose
    os.system('sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose')

    # Attribution des droits d'exécution à Docker Compose
    os.system('sudo chmod +x /usr/local/bin/docker-compose')


def install_sublime_text():
    # Installation de Sublime Text via Snap
    os.system('sudo snap install sublime-text --classic')


def main():
    update_packages()

    print("Installation de Docker...")
    install_docker()
    print("Installation de Docker Compose...")
    install_docker_compose()
    print("Installation de Sublime Text...")
    install_sublime_text()
    print("Installation terminée.")


if __name__ == '__main__':
    main()
