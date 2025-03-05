from automate import Automate

def main():
    nom_fichier = "automate.txt"
    try:
        automate = Automate.lire_fichier(nom_fichier)
        automate.afficher()
        print("L'automate est-il déterministe ?", automate.est_deterministe())
        print("L'automate est-il complet ?", automate.est_complet())
        print("L'automate est-il standard ?", automate.est_standard())
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")

if __name__ == "__main__":
    main()
