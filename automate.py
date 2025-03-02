class Automate:
    def __init__(self, alphabet, etats, etats_initiaux, etats_terminaux, transitions):
        self.alphabet = alphabet # liste des symboles
        self.etats = etats # liste des états
        self.etats_initiaux = etats_initiaux
        self.etats_terminaux = etats_terminaux
        self.transitions = transitions

    @classmethod
    def lire_fichier(cls, nom_fichier):
        with open(nom_fichier, "r") as f:
            lignes = [ligne.strip() for ligne in f.readlines()] # lit les lignes et les met dans une liste

        nb_symboles = int(lignes[0])
        alphabet = [chr(ord('a') + i) for i in range(nb_symboles)] # création de l'alphabet

        nb_etats = int(lignes[1])
        etats = list(range(nb_etats))

        etats_initiaux = list(map(int, lignes[2].split()[1:]))
        etats_terminaux = list(map(int, lignes[3].split()[1:]))

        nb_transitions = int(lignes[4])
        transitions = {etat: {} for etat in etats} # dictionnaire vide pour stocker les transitions

        for i in range(5, 5 + nb_transitions):
            etat_dep, symbole, etat_arr = int(lignes[i][0]), lignes[i][1], int(lignes[i][2])
            if symbole not in transitions[etat_dep]:
                transitions[etat_dep][symbole] = []
            transitions[etat_dep][symbole].append(etat_arr)

        return cls(alphabet, etats, etats_initiaux, etats_terminaux, transitions)

    def afficher(self):
        print(f"Alphabet : {self.alphabet}")
        print(f"États : {self.etats}")
        print(f"États initiaux : {self.etats_initiaux}")
        print(f"États terminaux : {self.etats_terminaux}")
        print("Transitions :")
        for etat, trans in self.transitions.items():
            for symbole, etats_suivants in trans.items():
                print(f"  {etat} --({symbole})--> {', '.join(map(str, etats_suivants))}")
