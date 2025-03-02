from automate import Automate

def main():
    nom_fichier = "automate.txt"
    try:
        automate = Automate.lire_fichier(nom_fichier)
        automate.afficher()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")

if __name__ == "__main__":
    main()
