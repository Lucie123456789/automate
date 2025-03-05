from automate import Automate
def main():
    nom_fichier = "automate.txt"
    try:
        automate = Automate.lire_fichier(nom_fichier)
        automate.afficher()
        print("L'automate est-il déterministe ?", automate.est_deterministe())
        print("L'automate est-il complet ?", automate.est_complet())
        print("L'automate est-il standard ?", automate.est_standard())
        print("Déterministe ?", automate.est_deterministe())
        print("Complet ?", automate.est_complet())
        print("Standard ?", automate.est_standard())

        if automate.est_deterministe() and automate.est_complet():
            partitions = automate.minimisation()
            print("Résultat de la minimisation:")
            print(partitions)
        else:
            print("L'automate doit être déterministe et complet avant minimisation.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")

if __name__ == "__main__":
    main()
