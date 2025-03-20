Projet : Manipulation d'Automates Finis
Description
Ce projet est une implémentation en Python d’un outil interactif pour manipuler des automates finis (AFN et AFD). Il permet de lire un automate depuis un fichier, d’afficher ses propriétés, d’effectuer diverses transformations (standardisation, déterminisation, complétion, minimisation), de tester la reconnaissance de mots, et de créer un automate complémentaire. Le programme gère également les ε-transitions, qui sont des transitions spontanées dans un AFN.

Le projet est conçu pour être utilisé via une interface utilisateur en ligne de commande, avec des menus interactifs pour guider l’utilisateur à travers les différentes fonctionnalités.

Fonctionnalités
Lecture d’un automate : Charge un automate depuis un fichier texte au format spécifié.
Affichage : Affiche les états initiaux, terminaux, et une table de référence des transitions (incluant les ε-transitions si présentes).
Vérification des propriétés :
Déterminisme : Vérifie si l’automate est déterministe.
Complétude : Vérifie si l’automate est complet.
Standardité : Vérifie si l’automate est standard.
Transformations :
Standardisation : Transforme l’automate en un automate standard (un seul état initial, sans transitions entrantes vers cet état).
Déterminisation : Convertit un AFN (avec ou sans ε-transitions) en un AFD.
Complétion : Ajoute un état puits pour rendre l’automate complet.
Minimisation : Minimise un automate déterministe et complet en utilisant l’algorithme de partitionnement.
Reconnaissance de mots : Teste si un mot donné est accepté par l’automate (nécessite un automate déterministe et complet).
Automate complémentaire : Crée un automate qui reconnaît le langage complémentaire (nécessite un automate déterministe et complet).
Prérequis
Python 3.6+ : Assurez-vous que Python est installé sur votre système.
Bibliothèque tabulate : Utilisée pour afficher les tables de transitions de manière lisible.
Installation
Clonez ou téléchargez ce projet dans un répertoire local :
git clone <url-du-projet>
cd <nom-du-projet>
Installez la bibliothèque tabulate via pip :
bash
pip install tabulate
Assurez-vous que le fichier automate.py (contenant le code principal) est dans le répertoire.
Structure des fichiers
automate.py : Le fichier principal contenant la classe Automate et l’interface utilisateur.
exemple_X.txt : Fichiers d’entrée contenant les automates (par exemple, automate1.txt).
Format des fichiers d’entrée
Les fichiers d’entrée doivent respecter le format suivant :

<nombre de symboles>
<nombre d'états>
<nombre d'états initiaux> <état initial 1> ... <état initial n>
<nombre d'états terminaux> <état terminal 1> ... <état terminal m>
<nombre de transitions>
<état de départ> <symbole> <état d'arrivée>
...
Les symboles de l’alphabet sont générés automatiquement comme a, b, c, ... (par exemple, si <nombre de symboles> = 2, l’alphabet est {a, b}).
Les états sont numérotés de 0 à <nombre d'états> - 1.
Le symbole "&" est utilisé pour les ε-transitions.
Exemple (exemple_1.txt) :

2
11
1 0
1 10
14
0 & 1
0 & 4
1 a 2
1 & 10
2 b 3
3 & 10
4 & 5
5 a 6
5 & 6
6 b 7
7 & 8
8 a 9
8 & 10
9 & 10
2 symboles (a, b)
11 états (0 à 10)
1 état initial (0)
1 état terminal (10)
14 transitions (dont plusieurs ε-transitions)
Utilisation
Lancez le programme :
bash
python automate.py
Suivez les menus interactifs :
Menu principal :
Choisir un automate (entrez un numéro pour charger automate<numero>.txt).
Quitter.
Menu automate :
Afficher l’automate.
Vérifier les propriétés (déterminisme, complétude, standardité).
Standardiser l’automate.
Déterminiser et compléter.
Minimiser l’automate.
Tester des mots.
Créer l’automate complémentaire.
Retour au menu principal.
Exemple d’utilisation
Lancez le programme :
bash

python automate.py
Au menu principal, entrez 1 pour choisir un automate, puis entrez test pour charger automate_test.txt.
Au menu automate, entrez 1 pour afficher l’automate :
text

États initiaux : 0
États terminaux : 10

Tableau de référence :
+-------+-----+-----+-------+
| État  |  a  |  b  |   ε   |
+-------+-----+-----+-------+
| E0    | --  | --  | 1,4   |
| 1     | 2   | --  | 10    |
| 2     | --  | 3   | --    |
| 3     | --  | --  | 10    |
| 4     | --  | --  | 5     |
| 5     | 6   | --  | 6     |
| 6     | --  | 7   | --    |
| 7     | --  | --  | 8     |
| 8     | 9   | --  | 10    |
| 9     | --  | --  | 10    |
| S10   | --  | --  | --    |
+-------+-----+-----+-------+
Entrez 4 pour déterminiser et compléter l’automate, puis 1 pour afficher le résultat :
text

Correspondance des états après déterminisation :
État 0 : 0,1,4,5,6,10
État 1 : 2,3,6,7,8,10
État 2 : 7,8,10
État 3 : 9,10
L'automate a été déterminisé (avec prise en compte des ε-transitions).
L'automate a été complété.

États initiaux : 0
États terminaux : 0,1,2,3

Tableau de référence :
+-------+----------+-------+
| État  |    a     |   b   |
+-------+----------+-------+
| E0    | 1        | 2     |
| S1    | 3        | 2     |
| S2    | 3        | 4     |
| S3    | 4        | 4     |
| 4     | 4        | 4     |
+-------+----------+-------+
Entrez 6 pour tester des mots :
text

Entrez un mot à tester (ou 'fin' pour quitter) : ab
Le mot 'ab' est accepté.
Entrez un mot à tester (ou 'fin' pour quitter) : fin
Détails techniques
Gestion des ε-transitions :
Les ε-transitions sont gérées lors de la déterminisation en calculant les fermetures ε.
La table de transition affiche une colonne "&" uniquement s’il existe des ε-transitions et dans ce cas elle est considirée comme une table de référence.

Affichage :
Les tables sont affichées avec tabulate pour une présentation claire.
Renumérotation des états :
Après minimisation, les états sont renumérotés en entiers pour simplifier les opérations ultérieures.
Les correspondances entre les anciens et nouveaux états sont affichées lors des transformations (déterminisation, minimisation).
Limitations
Les automates doivent être définis dans des fichiers au format spécifié.
La reconnaissance de mots et la création de l’automate complémentaire nécessitent un automate déterministe et complet (le programme effectue automatiquement la déterminisation et la complétion si nécessaire).
Les performances peuvent être affectées pour des automates très grands, en raison de la complexité exponentielle de la déterminisation.
Contribution
Pour contribuer à ce projet :

Forkez le dépôt.
Créez une branche pour vos modifications :
bash

git checkout -b feature/nouvelle-fonctionnalite
Effectuez vos modifications et testez-les.
Soumettez une pull request.
Auteurs
[Votre nom] - Développeur principal
Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
