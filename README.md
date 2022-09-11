# OpenClassrooms_projet_2_Loic
# Version béta d'un programme de scraping.

Le programme suivant, créé dans le cadre du projet 4 du parcours d'OpenClassrooms, est un gestionnaire de tournois d'échecs 

Actuellement voici les fonctionnalités du programme : 

1. Créer un tournoi

2. Créer et/ou Ajouter des joueurs

3. Jouer un tournoi sous la forme : tour | match

4. Sauvegarder et/ou charger un tournoi

5. Créer des rapports (Voir le classement des joueurs, historique des matchs)

## Pré-requis 

* Python 3 installé ([Télécharger Python](https://www.python.org/downloads/))
* Git ([Télécharger Git](https://github.com/))

## Installation

Pour la suite des instructions je conseille aux utilisateurs de Windows d'utiliser ([gitbash](https://git-scm.com/downloads))

1. **Téléchargement du projet.**


    Depuis votre terminal, placez-vous à l'endroit souhaité:
    
    ```cd [chemin d'accès]```  
    
    Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```

    Copier le programme source:

    ```git clone https://github.com/Lockco/Open-Classrooms-Projet-4```
    
2. **Creer un environnement virtuel.**

    Depuis windows/mac/linux: ```python3 -m venv env``` ou ```py -m venv env```
    
3. **Activer l'environnement.**
    
    Depuis windows: ``` source env\Scripts\activate.bat``` si cette commande ne fonctionne pas essayer la commande suivante : ```source env\Scripts\activate```
    
    Depuis mac/linux: ```source env/bin/activate```

4. **Installer les paquets.**

    Attention : pour éviter de rencontrer des problème avec ```pip``` veillez à vérifier que PYTHONPATH soit correctement configurées : 
    ([PYTHONPATH](https://datatofish.com/add-python-to-windows-path/))
    
    L'installation des paquets se fait en exécutant la commande suivante : ```pip install -r requirements.txt```
    
5. **Lancement du programme**

    Pour le démarrage du programme dans votre terminal verifier que vous êtes dans le dossier 
    où le projet a été cloné avec la commande suivante

    Sous linux : ```ls``` 
    Sous windows : ```dir```
    
    
    puis lancer le script à l'aide de la commande suivante :

    ```py __main__.py```

6. **Générer le rapport Flake8.**

    - Installer flake8 avec la commande suivante : ```pip install flake8-html```

    - Créer un fichier setup.cfg contenant le texte suivant :

    ``` [flake8] max-line-length = 119
        exclude =
        .git,
        __pycache__,
        venv
    ```
    
    - Exécuter la commande suivante : ```flake8 --format=html --htmldir=flake-report --exclude=env/```
## Logiciel utilisé
[Visual Studio Code] (https://code.visualstudio.com/download)
[gitbash] (https://git-scm.com/downloads)

## Remerciements

Merci à **Julien**, **Thibault**, pour leur patience et leur aide précieuse.
