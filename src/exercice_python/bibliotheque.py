from exercice_python.base_bibliotheque import BaseBibliotheque

# ✅ Classe qui hérite de la classe abstraite
class Bibliotheque(BaseBibliotheque):
    """Classe concrète qui implémente la bibliothèque classique"""

    def ajouter_livre(self, titre, auteur):
        """Implémentation de la méthode abstraite"""
        self.livres[titre] = auteur
        print(f"📖 Livre '{titre}' ajouté avec succès !")

    def livres_disponibles(self):
        ##Completer ici
