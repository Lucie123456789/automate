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
Choisissez l'option 1 pour charger un automate (par exemple, entrez 9 pour charger Automates_tests/exemple_9.txt).
Utilisez les options du menu pour effectuer des transformations (affichage, vérification des propriétés, déterminisation, minimisation, etc.).
Les traces d'exécution sont automatiquement enregistrées dans le répertoire traces/ (par exemple, traces/trace_exemple_32.txt).
Exemple de trace
Voici un extrait d'une trace générée pour l'automate exemple_9.txt :

text
Trace de l'automate Automates_tests/exemple_9.txt

Automate lu avec succès depuis Automates_tests/exemple_9.txt.

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

--- Affichage de l'automate ---
États initiaux : 1
États terminaux : 0

Table de transitions :
+------+----+----+
| État | a  | b  |
+------+----+----+
|  S0  | -- | -- |
|  E1  | 2  | -- |
|  2   | 3  | 3  |
|  3   | 4  | -- |
|  4   | 5  | 5  |
|  5   | 0  | -- |
+------+----+----+

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

--- Vérification des propriétés ---
Déterministe : True
L'automate n'est pas complet : aucune transition depuis l'état 0.
Complet : False
Standard : True

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

--- Standardisation ---
L'automate est déjà standard.

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

--- Déterminisation et complétion ---
L'automate est déterministe.
L'automate n'est pas complet : aucune transition depuis l'état 0.
Complétion de l'automate déterministe.
L'automate n'est pas complet : aucune transition depuis l'état 0.
L'automate a été complété.
États initiaux : 1
États terminaux : 0

Table de transitions :
+------+---+---+
| État | a | b |
+------+---+---+
|  S0  | 6 | 6 |
|  E1  | 2 | 6 |
|  2   | 3 | 3 |
|  3   | 4 | 6 |
|  4   | 5 | 5 |
|  5   | 0 | 6 |
|  6   | 6 | 6 |
+------+---+---+

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

--- Minimisation ---
Minimisation de l'automate.
L'automate est déjà déterministe et complet.
Partition initiale :
Groupe 0 : 0
Groupe 1 : 1, 2, 3, 4, 5, 6
Partition après raffinement :
Groupe 0 : 0
Groupe 1 : 1
Groupe 2 : 2
Groupe 3 : 3
Groupe 4 : 4
Groupe 5 : 5
Groupe 6 : 6
Partition après raffinement :
Groupe 0 : 0
Groupe 1 : 1
Groupe 2 : 2
Groupe 3 : 3
Groupe 4 : 4
Groupe 5 : 5
Groupe 6 : 6
Correspondance des états après minimisation :
État 0 : 0
État 1 : 1
État 2 : 2
État 3 : 3
État 4 : 4
État 5 : 5
État 6 : 6
L'automate a été minimisé.
États initiaux : 1
États terminaux : 0

Table de transitions :
+------+---+---+
| État | a | b |
+------+---+---+
|  S0  | 6 | 6 |
|  E1  | 2 | 6 |
|  2   | 3 | 3 |
|  3   | 4 | 6 |
|  4   | 5 | 5 |
|  5   | 0 | 6 |
|  6   | 6 | 6 |
+------+---+---+

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

--- Test de mots ---
Le mot 'a' est rejeté.
Le mot 'aaa' est rejeté.
Le mot 'b' est rejeté.
Le mot 'bb' est rejeté.
Le mot 'bbbaaa' est rejeté.
Le mot 'aabbbaaa' est rejeté.
Le mot '' est rejeté.

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

--- Création de l'automate complémentaire ---
L'automate complémentaire a été construit.
États initiaux : 1
États terminaux : 1, 2, 3, 4, 5, 6

Table de transitions :
+------+---+---+
| État | a | b |
+------+---+---+
|  0   | 6 | 6 |
| ES1  | 2 | 6 |
|  S2  | 3 | 3 |
|  S3  | 4 | 6 |
|  S4  | 5 | 5 |
|  S5  | 0 | 6 |
|  S6  | 6 | 6 |
+------+---+---+

=== Menu Automate ===
1. Afficher l'automate
2. Vérifier les propriétés
3. Standardiser l'automate
4. Déterminiser et compléter
5. Minimiser l'automate
6. Tester des mots
7. Créer l'automate complémentaire
8. Retour au menu principal

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
