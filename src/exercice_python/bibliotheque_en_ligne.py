from exercice_python.bibliotheque import Bibliotheque

# ✅ Classe enfant qui hérite de Bibliotheque et ajoute la gestion des emprunts
class BibliothequeEnLigne(Bibliotheque):
    def __init__(self):
        """Initialise la bibliothèque en ligne avec un dictionnaire pour les emprunts"""
        super().__init__()
        self.emprunts = {}  # Dictionnaire {titre: emprunteur}

    def emprunter_livre(self, titre, emprunteur):
        """Permet d’emprunter un livre si disponible"""
        if titre in self.livres and titre not in self.emprunts:
            self.emprunts[titre] = emprunteur
            print(f"📚 '{titre}' emprunté par {emprunteur}.")
        elif titre in self.emprunts:
            print(f"❌ Le livre '{titre}' est déjà emprunté par {self.emprunts[titre]}.")
        else:
            print(f"❌ Le livre '{titre}' n'est pas disponible dans la bibliothèque.")

    def rendre_livre(self, titre):
        """Permet de rendre un livre emprunté"""
        if titre in self.emprunts:
            del self.emprunts[titre]
            print(f"✅ Le livre '{titre}' a été rendu.")
        else:
            print(f"❌ Le livre '{titre}' n'est pas emprunté.")

    def livres_disponibles(self):
        """Retourne les livres qui ne sont pas empruntés"""
        return [titre for titre in self.livres.keys() if titre not in self.emprunts]
