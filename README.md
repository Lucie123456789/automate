README - Projet Automates Finis et Expressions Rationnelles
Description
Ce projet, réalisé dans le cadre du cours Automates Finis et Expressions Rationnelles (EFREI P2 2024/2025), implémente un programme Python pour manipuler des automates finis non déterministes (AFN) avec ε-transitions. Le programme permet de charger un automate à partir d'un fichier texte, d'effectuer diverses transformations (standardisation, déterminisation, complétion, minimisation, etc.), et de tester des mots. Les traces d'exécution sont générées automatiquement pour documenter les transformations et les tests.

Fonctionnalités principales
Chargement d'un automate : Lecture d'un automate à partir d'un fichier texte (par exemple, Automates_tests/exemple_32.txt).
Affichage : Affichage de l'automate sous forme de table de transitions, avec prise en charge des ε-transitions.
Vérification des propriétés : Vérification si l'automate est déterministe, complet, et standard.
Standardisation : Transformation de l'automate en un automate standard (un seul état initial, pas de transitions entrantes vers l'état initial).
Déterminisation et complétion : Conversion de l'AFN en un automate fini déterministe (AFD) complet, avec prise en compte des ε-transitions.
Minimisation : Minimisation de l'automate déterministe et complet en utilisant l'algorithme de partitionnement (Hopcroft).
Test de mots : Vérification si un mot est accepté par l'automate (nécessite un automate déterministe et complet).
Automate complémentaire : Création de l'automate complémentaire (nécessite un automate déterministe et complet).
Génération de traces : Enregistrement des traces d'exécution dans des fichiers texte (par exemple, traces/trace_exemple_32.txt).
Changements récents
Gestion des ε-transitions : Les ε-transitions sont maintenant correctement prises en compte lors de la déterminisation, en utilisant la fermeture ε pour calculer les nouveaux états.
Renumérotation des états : Après la déterminisation, les états (qui étaient des frozenset) sont renumérotés en entiers pour simplifier les manipulations et l'affichage.
Encodage UTF-8 : Les fichiers de trace sont générés avec un encodage UTF-8, et la console est configurée pour gérer les caractères Unicode (nécessaires pour les tables générées par tabulate).
Minimisation améliorée : La méthode minimiser s'assure que l'automate est déterministe et complet avant de procéder à la minimisation, en appelant determiniser_et_completer si nécessaire.
Correction de bugs :
Résolution des erreurs d'encodage (UnicodeEncodeError) en forçant l'encodage UTF-8 pour sys.stdout.
Résolution des erreurs liées à la gestion des frozenset dans la minimisation.
Correction d'une UnboundLocalError dans minimiser en s'assurant que la variable automate est toujours définie.
Structure du projet
Fichiers principaux :
automate.py : Contient le code source principal, y compris la classe Automate et la fonction main.
Automates_tests/ : Répertoire contenant les fichiers d'automates de test (par exemple, exemple_32.txt).
traces/ : Répertoire où sont générées les traces d'exécution (par exemple, trace_exemple_32.txt).
Dépendances :
Python 3.6 ou supérieur (recommandé : Python 3.7+ pour une meilleure gestion de l'encodage).
Bibliothèque tabulate pour l'affichage des tables (installable via pip install tabulate).
Installation et exécution
Prérequis
Assurez-vous que Python 3 est installé sur votre système :
bash

python --version
Si ce n'est pas le cas, téléchargez et installez Python depuis python.org.
Installez la bibliothèque tabulate :
bash

pip install tabulate
Exécution
Clonez ou téléchargez le projet dans un répertoire local.
Placez-vous dans le répertoire du projet :
bash

cd chemin/vers/le/projet
Exécutez le programme :
bash

python automate.py
Suivez les instructions du menu interactif pour charger un automate et effectuer des transformations.
Exemple d'utilisation
Lancez le programme :
bash

python automate.py
Choisissez l'option 1 pour charger un automate (par exemple, entrez 32 pour charger Automates_tests/exemple_32.txt).
Utilisez les options du menu pour effectuer des transformations (affichage, vérification des propriétés, déterminisation, minimisation, etc.).
Les traces d'exécution sont automatiquement enregistrées dans le répertoire traces/ (par exemple, traces/trace_exemple_32.txt).
Exemple de trace
Voici un extrait d'une trace générée pour l'automate exemple_32.txt :

text

Trace de l'automate Automates_tests/exemple_32.txt

Automate lu avec succès depuis Automates_tests/exemple_32.txt.

--- Affichage de l'automate ---
États initiaux : 0
États terminaux : 21

Table de transitions :
+------+----+----+----+----+-------+
| État | a  | b  | c  | d  |   &   |
+------+----+----+----+----+-------+
|  E0  | -- | -- | -- | -- | 1,10  |
|  1   | -- | -- | -- | -- |  2,6  |
|  2   | -- | -- | -- | -- |  3,5  |
|  3   | -- | 4  | -- | -- |  --   |
|  4   | -- | -- | -- | -- |  3,5  |
|  5   | -- | -- | -- | -- |   8   |
|  6   | 7  | -- | -- | -- |  --   |
|  7   | -- | -- | -- | -- |   8   |
|  8   | -- | -- | 9  | -- |  --   |
|  9   | -- | -- | -- | -- |  21   |
|  10  | -- | -- | -- | -- | 11,15 |
|  11  | -- | -- | -- | -- | 12,14 |
|  12  | 13 | -- | -- | -- |  --   |
|  13  | -- | -- | -- | -- | 12,14 |
|  14  | -- | -- | -- | -- |  17   |
|  15  | -- | 16 | -- | -- |  --   |
|  16  | -- | -- | -- | -- |  17   |
|  17  | -- | -- | -- | -- | 18,20 |
|  18  | -- | -- | 19 | -- |  --   |
|  19  | -- | -- | -- | -- | 18,20 |
|  20  | -- | -- | -- | -- |  21   |
| S21  | -- | -- | -- | -- |  --   |
+------+----+----+----+----+-------+

--- Vérification des propriétés ---
L'automate n'est pas déterministe : plusieurs transitions depuis l'état 0 avec le symbole '&'.
Déterministe : False
L'automate n'est pas complet : il manque une transition depuis l'état 0 avec le symbole 'a'.
Complet : False
Standard : True

--- Déterminisation et complétion ---
L'automate a été déterminisé.
L'automate a été complété.

--- Minimisation ---
L'automate est déjà déterministe et complet.
Partition initiale :
Groupe 0 : frozenset({0, 1, 2, 3, 5, 6, 8, 10, 11, 12, 14, 15, 17, 18, 20, 21}), frozenset({18, 19, 20, 21, 9}), frozenset({3, 4, 5, 8, 16, 17, 18, 20, 21}), frozenset({17, 18, 20, 21, 12, 13, 14}), frozenset({9, 21}), frozenset({18, 19, 20, 21}), frozenset({7, 8, 12, 13, 14, 17, 18, 20, 21})
Groupe 1 : frozenset({8, 3, 4, 5}), frozenset({22})
L'automate a été minimisé.

--- Test de mots ---
Le mot 'abcd' est rejeté.
Le mot 'aaabbbbbcccdddddddddddd' est rejeté.
Le mot 'aaaaaaaaaaa' est accepté.
Le mot 'ccccccc' est accepté.
Contenu du rendu
Conformément aux instructions du projet (EFREI P2 2024/2025) :

Code source :
Fichier : Automate.py
Contient le code complet, y compris la gestion des ε-transitions et la génération des traces.
Traces d'exécution :
Répertoire : traces/
Fichiers générés pour chaque automate testé (par exemple, trace_exemple_32.txt).
Les traces incluent toutes les transformations et tests demandés (affichage, vérification des propriétés, standardisation, déterminisation, minimisation, test de mots, automate complémentaire).
Fichier README (facultatif) :
Un fichier PDF expliquant le travail.
Problèmes connus et solutions
Encodage sur Windows :
Problème : Les caractères Unicode utilisés par tabulate provoquaient des erreurs d'encodage (UnicodeEncodeError) sur Windows.
Solution : Forcer l'encodage UTF-8 pour sys.stdout avec io.TextIOWrapper (compatible avec Python < 3.7) ou sys.stdout.reconfigure (Python 3.7+).
Gestion des frozenset :
Problème : Après la déterminisation, les états étaient des frozenset, ce qui compliquait la minimisation.
Solution : Les états sont renumérotés en entiers dans determiniser, et minimiser fonctionne avec des entiers.
Variable non définie dans minimiser :
Problème : Une UnboundLocalError se produisait si l'automate était déjà déterministe et complet.
Solution : Ajout d'un bloc else pour s'assurer que la variable automate est toujours définie.
Améliorations futures
Ajouter une interface graphique pour visualiser les automates.
Optimiser l'algorithme de minimisation pour des automates de grande taille.
Ajouter des tests unitaires pour valider chaque méthode de la classe Automate.
Auteurs
[KABORE Boudnoma B. Fortune] [IDOUFKIR Marouane] [LABAT Aude] [OZGULLU Lucie] [HAJI Myriam] - Étudiants à l'EFREI Paris, P2 Promo 2028.
Remerciements
Merci aux enseignants Helen KASSEL et Olga MELEKHOVA pour leur encadrement et leurs conseils.
Merci à l'assistant IA Grok (xAI) pour son aide dans le débogage et la rédaction de ce README.
