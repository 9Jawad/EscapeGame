# Escape Game
![image](https://github.com/user-attachments/assets/6ccc2d4b-4733-408d-a2ae-e18ff4c6d468)

## Description
Ce projet est un jeu d'évasion (escape game) où le joueur contrôle un personnage se déplaçant dans un château représenté en plan. Le château est constitué de pièces, couloirs, murs, portes et objets. Le but du jeu est d'atteindre la sortie du château en répondant à des questions pour ouvrir les portes et en ramassant des objets.

## Fichiers
- `CONFIGS.py` : Contient les configurations du jeu telles que les couleurs, les dimensions et les fichiers de données.
- `chateau.py` : Contient le code principal du jeu, y compris l'affichage du plan, la gestion des déplacements et des interactions avec les objets et les portes.

## Installation
1. Assurez-vous d'avoir Python installé sur votre machine.
2. Clonez ce dépôt ou téléchargez les fichiers `CONFIGS.py` et `chateau.py`.

## Utilisation
1. Placez les fichiers de données (`plan_chateau.txt`, `dico_portes.txt`, `dico_objets.txt`) dans le même répertoire que les fichiers Python.
2. Exécutez le fichier `chateau.py` pour démarrer le jeu :
   ```bash
   python3 chateau.py
   ```
3. Utilisez les touches fléchées pour déplacer le personnage dans le château.

## Configuration
Vous pouvez modifier les configurations du jeu dans le fichier `CONFIGS.py` :
- Coordonnées des zones d'affichage
- Couleurs des cases, murs, portes, objets, etc.
- Position de départ du personnage
- Fichiers de données à utiliser

## Auteur
Jawad Cherkaoui

## Date
7 novembre 2022

## Licence
Ce projet est sous licence MIT.
