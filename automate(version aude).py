import re
import os

class Automate:
    def __init__(self):
        """Initialisation de l'automate avec des ensembles vides."""
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.initial_states = set()
        self.final_states = set()

    def est_complet(self):
        """Vérifie si l'automate est complet (chaque état a une transition pour chaque symbole)."""
        for state in self.states:
            for symbol in self.alphabet:
                if (state, symbol) not in self.transitions:
                    return False
        return True

    def est_deterministe(self):
        """
        Vérifie si l'automate est déterministe :
        - Il doit être **complet**.
        - Il ne doit pas y avoir d'état avec plusieurs transitions sur un même symbole.
        - Il ne doit avoir qu'un seul état initial.
        """
        if not self.est_complet():
            return False  # Un automate non complet n'est jamais déterministe

        if len(self.initial_states) > 1:
            return False

        for (state, symbol), destinations in self.transitions.items():
            if len(destinations) > 1:
                return False
        return True

    def completer(self):
        """Ajoute un état 'poubelle' si l'automate n'est pas complet."""
        if self.est_complet():
            return

        poubelle = 'P'
        self.states.add(poubelle)

        for state in self.states:
            for symbol in self.alphabet:
                if (state, symbol) not in self.transitions:
                    self.transitions[(state, symbol)] = {poubelle}

        for symbol in self.alphabet:
            self.transitions[(poubelle, symbol)] = {poubelle}

   
    def determiniser(self):
        """Déterminise l'automate après l'avoir complété si nécessaire."""
        if self.est_deterministe():
            return self

        self.completer()  # On complète d'abord pour s'assurer qu'on peut déterminiser

        new_automate = Automate()
        new_queue = [list(self.initial_states)]
        new_state_map = {self._nom_etat(new_queue[0]): new_queue[0]}
        new_automate.initial_states = {self._nom_etat(new_queue[0])}

        while new_queue:
            current_states = new_queue.pop(0)
            current_state_name = self._nom_etat(current_states)
            new_automate.states.add(current_state_name)

            for symbol in self.alphabet:
                next_states = set()
                for state in current_states:
                    next_states.update(self.transitions.get((state, symbol), set()))

                if next_states:
                    next_state_name = self._nom_etat(next_states)
                    if next_state_name not in new_state_map:
                        new_state_map[next_state_name] = list(next_states)
                        new_queue.append(list(next_states))
                    new_automate.transitions[(current_state_name, symbol)] = {next_state_name}

            if set(current_states) & self.final_states:
                new_automate.final_states.add(current_state_name)

        new_automate.alphabet = self.alphabet
        return new_automate
    
    def est_standard(self):
        """Vérifie si l'automate est standard."""
        if len(self.initial_states) != 1:
            return False  # Il doit y avoir un seul état initial

        initial_state = next(iter(self.initial_states))  # Récupère l'état initial
        for (etat, _), destinations in self.transitions.items():
            if initial_state in destinations:
                return False  # L'état initial ne doit pas être une destination
        return True

    def standardiser(self):
        """Transforme l'automate en un automate standard."""
        if self.est_standard():
            return

        nouvel_etat_initial = "I"  # Nouveau nom pour éviter les conflits
        self.states.add(nouvel_etat_initial)
        self.initial_states = {nouvel_etat_initial}

        # Créer des transitions vers les anciens états initiaux
        for etat_init in list(self.initial_states):
            for symbole in self.alphabet:
                if (etat_init, symbole) in self.transitions:
                    self.transitions.setdefault((nouvel_etat_initial, symbole), set()).update(self.transitions[(etat_init, symbole)])


    def _nom_etat(self, etats):
        """Génère un nom unique pour un état composé de plusieurs sous-états."""
        return ''.join(sorted(etats))

    def lire_depuis_fichier(self, chemin):
        """Charge un automate depuis un fichier texte respectant le format spécifié."""
        try:
            with open(chemin, 'r') as f:
                lignes = [ligne.strip() for ligne in f if ligne.strip()]
        except FileNotFoundError:
            print(f"Erreur : Le fichier {chemin} est introuvable.")
            return False
    

        # Lecture des informations
        index = 0
        nb_symboles = int(lignes[index])
        index += 1
        nb_etats = int(lignes[index])
        index += 1
        
        # États initiaux
        init_data = list(map(int, lignes[index].split()))
        nb_etats_initiaux = init_data[0]
        self.initial_states = set(map(str, init_data[1:]))
        index += 1

        # États terminaux
        final_data = list(map(int, lignes[index].split()))
        nb_etats_terminaux = final_data[0]
        self.final_states = set(map(str, final_data[1:]))
        index += 1

        # Nombre de transitions
        nb_transitions = int(lignes[index])
        index += 1

        # Lire les transitions
        for i in range(nb_transitions):
            etat_depart, symbole, etat_arrivee = lignes[index].split()
            self.states.update([etat_depart, etat_arrivee])
            self.alphabet.add(symbole)
            self.transitions.setdefault((etat_depart, symbole), set()).add(etat_arrivee)
            index += 1
        
        return True

    def afficher(self):
        print("\n=== Automate ===")
        print("Alphabet :", " ".join(sorted(self.alphabet)))
        print("États :", " ".join(sorted(self.states)))
        print("États initiaux :", " ".join(sorted(self.initial_states)))
        print("États finaux :", " ".join(sorted(self.final_states)))
    
        print("\nTable de transitions :")

        # Affichage de l'en-tête
        header = f"{'Etat':<12} | " + " | ".join(f"{symbole:<10}" for symbole in sorted(self.alphabet))
        print(header)
        print("-" * len(header))

        for state in sorted(self.states):
            etat_label = ""
            if state in self.initial_states:
                etat_label += "E "  # Marqueur pour état initial

            elif state in self.final_states:
                etat_label += "S "  # Marqueur pour état final
            else:
                etat_label += "  "

            row = [f"{etat_label}{state:<8} |"]
            for symbole in sorted(self.alphabet):
                destinations = self.transitions.get((state, symbole), set())
                row.append(f"{','.join(sorted(destinations)) if destinations else '-':<10}")
        
            print(" ".join(row))

        print("\nDéterministe :", "Oui" if self.est_deterministe() else "Non")
        print("Complet :", "Oui" if self.est_complet() else "Non")
        print("Standard :", "Oui" if self.est_standard() else "Non")
        print("Minimiser :", "Oui" if self.est_standard() else "Non")

    def complementaire(self):
        """
        Calcule et retourne l'automate complémentaire.
        
        L'automate complémentaire est obtenu en prenant un automate déterministe et complet
        et en inversant ses états finaux (les anciens états finaux deviennent non finaux et vice versa).
        """
        
        # L'automate doit être déterministe et complet
        if not self.est_deterministe():
            print("L'automate n'est pas déterministe. Déterminisation en cours...")
            automate = self.determiniser()
        else:
            automate = self

        if not automate.est_complet():
            print("L'automate n'est pas complet. Complétion en cours...")
            automate.completer()

        # Création de l'automate complémentaire
        automate_complementaire = Automate()
        automate_complementaire.states = automate.states.copy()
        automate_complementaire.alphabet = automate.alphabet.copy()
        automate_complementaire.transitions = automate.transitions.copy()
        automate_complementaire.initial_states = automate.initial_states.copy()
        
        # Les nouveaux états finaux sont ceux qui n'étaient pas finaux dans l'automate original
        automate_complementaire.final_states = automate.states - automate.final_states
        
        print("Automate complémentaire construit avec succès.")
        return automate_complementaire

    def afficher_tableau(self):
        """Affiche un tableau clair des transitions"""
        print("\nTableau des transitions de l'automate minimisé :")
        header = "Etat" + " | " + " | ".join(sorted(self.alphabet))
        print(header)
        print("-" * len(header))
        for state in sorted(self.states):
            row = [state]
            for symbol in sorted(self.alphabet):
                destinations = self.transitions.get((state, symbol), set())
                row.append(",".join(sorted(destinations)) if destinations else "-")
            print(" | ".join(row))
        print("\n")



    def est_minimise(self, automate_original):
        """Vérifie si l'automate a été minimisé."""
        return len(self.states) == len(automate_original.states)

    def minimisation(self):
        """Minimise l'automate en regroupant les états équivalents de manière déterministe."""
        
        # Séparation des états finaux et non finaux
        partition = [set(self.final_states), self.states - set(self.final_states)]
        changement = True  

        while changement:
            changement = False
            nouvelle_partition = []

            # Tri pour garantir un ordre stable
            partition = sorted(partition, key=lambda p: sorted(p))

            for groupe in partition:
                sous_partitions = {}

                for etat in groupe:
                    signature = tuple(
                        next((i for i, part in enumerate(partition) if self.transitions.get((etat, sym)) in part), -1)
                        for sym in sorted(self.alphabet)
                    )
                    sous_partitions.setdefault(signature, set()).add(etat)

                nouvelle_partition.extend(sous_partitions.values())
                if len(sous_partitions) > 1:
                    changement = True

            partition = nouvelle_partition

        # Création d'un automate minimisé avec un ordre déterministe
        automate_minimise = Automate()
        automate_minimise.alphabet = self.alphabet

        # Toujours prendre l'état le plus petit comme représentant
        etat_representant = {etat: sorted(part)[0] for part in partition for etat in part}

        for part in partition:
            representant = sorted(part)[0]  # Toujours le premier état trié
            automate_minimise.states.add(representant)

            if representant in self.initial_states:
                automate_minimise.initial_states.add(representant)
            if representant in self.final_states:
                automate_minimise.final_states.add(representant)

        for etat in sorted(self.states):
            representant = etat_representant[etat]
            for symbole in sorted(self.alphabet):
                next_states = sorted(self.transitions.get((etat, symbole), set()))
                for next_state in next_states:
                    automate_minimise.transitions.setdefault((representant, symbole), set()).add(etat_representant[next_state])

        print("\nMinimisation effectuée avec succès.")
        automate_minimise.afficher_tableau()
        
        return automate_minimise


if __name__ == "__main__":
    fichier_automate = "automate2.txt"  # Remplace par ton fichier

    # Création et affichage initial de l'automate
    automate = Automate()
    if not automate.lire_depuis_fichier(fichier_automate):
        print("Arrêt du programme en raison de l'échec de la lecture.")
        exit(1)

    print("\nAutomate initial :")
    automate.afficher()  # Affichage initial avant minimisation

    # Complétion
    if not automate.est_complet():
        print("\nL'automate n'est pas complet. Complétion en cours...")

    # Déterminisation (nécessite un automate complet)
    if not automate.est_deterministe():
        print("\nL'automate n'est pas déterministe. Déterminisation en cours...")
        automate = automate.determiniser()
        automate.afficher()  # Affiche l'automate après déterminisation

    # Standardisation
    if automate.est_standard():
        print("\nL'automate est déjà standard.")
    else:
        print("\nL'automate n'est pas standard. Standardisation en cours...")
        automate.standardiser()
        automate.afficher()  # Affiche l'automate après standardisation

    # Complémentaire
    print("\nConstruction de l'automate complémentaire...")
    automate_complementaire = automate.complementaire()
    automate_complementaire.afficher()

    # Minimisation
    print("\nMinimisation en cours...")
    automate_minimise = automate.minimisation()

