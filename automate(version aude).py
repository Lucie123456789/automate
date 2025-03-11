import re

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
        """Charge un automate depuis un fichier texte."""
        with open(chemin, 'r') as f:
            lignes = [ligne.strip() for ligne in f if ligne.strip()]

        self.alphabet = set(re.split(r'\s+', lignes[0]))
        self.states = set(re.split(r'\s+', lignes[1]))
        self.initial_states = set(re.split(r'\s+', lignes[2]))
        self.final_states = set(re.split(r'\s+', lignes[3]))

        for ligne in lignes[4:]:
            source, symbole, destination = re.split(r'\s+', ligne)
            self.transitions.setdefault((source, symbole), set()).add(destination)

    def afficher(self):
        """Affiche l'automate sous forme lisible."""
        print('=== Automate ===')
        print('Alphabet :', ' '.join(sorted(self.alphabet)))
        print('États :', ' '.join(sorted(self.states)))
        print('États initiaux :', ' '.join(sorted(self.initial_states)))
        print('États finaux :', ' '.join(sorted(self.final_states)))
        print('\nTable de transitions :')

        print(f"{'État':<10} " + ' '.join(f'{symbole:<10}' for symbole in sorted(self.alphabet)))
        print('-' * (12 + 12 * len(self.alphabet)))

        for state in sorted(self.states):
            row = [f'{state:<10}']
            for symbole in sorted(self.alphabet):
                destinations = self.transitions.get((state, symbole), set())
                row.append(','.join(sorted(destinations)).ljust(10) if destinations else '-'.ljust(10))
            print(' '.join(row))

        print(f"\nDéterministe : {'Oui' if self.est_deterministe() else 'Non'}")
        print(f"Complet : {'Oui' if self.est_complet() else 'Non'}")
        print(f"Standard : {'Oui' if self.est_standard() else 'Non'}")  # 🔹 Ajout de l'affichage de la standardisation

if __name__ == "__main__":
    """Point d'entrée du programme : teste déterminisation, standardisation, complétion."""
    fichier_automate = "automate2.txt"  # Remplace par ton fichier

    # Création et affichage initial de l'automate
    automate = Automate()
    automate.lire_depuis_fichier(fichier_automate)
    print("\nAutomate initial :")
    automate.afficher()

    # Complétion
    if not automate.est_complet():
        print("\nL'automate n'est pas complet. Complétion en cours...")
        automate.completer()
        automate.afficher()

    # Déterminisation (nécessite un automate complet)
    if not automate.est_deterministe():
        print("\nL'automate n'est pas déterministe. Déterminisation en cours...")
        automate = automate.determiniser()
        automate.afficher()

    # Standardisation
    if automate.est_standard():
        print("\nL'automate est déjà standard.")
    else:
        print("\nL'automate n'est pas standard. Standardisation en cours...")
        automate.standardiser()
        automate.afficher()
