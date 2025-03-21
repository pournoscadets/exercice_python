from abc import ABC, abstractmethod


# ✅ Classe abstraite
class BaseBibliotheque(ABC):
    """Classe abstraite pour définir les bibliothèques"""

    def __init__(self):
        self.livres = {}  # Dictionnaire {titre: auteur}

    @abstractmethod
    def ajouter_livre(self, titre, auteur):
        """Méthode abstraite que toutes les bibliothèques doivent implémenter"""
        pass

    def supprimer_livre(self, titre):
        """Supprime un livre si présent, sinon lève une exception"""
        if titre in self.livres:
            del self.livres[titre]
            print(f"🗑️ Livre '{titre}' supprimé !")
        else:
            raise ValueError(f"❌ Erreur : Le livre '{titre}' n'existe pas.")

    def rechercher_par_auteur(self, auteur):
        """Recherche tous les livres d'un auteur donné"""
        livres_auteur = list(filter(lambda item: item[1] == auteur, self.livres.items()))
        if livres_auteur:
            return [titre for titre, _ in livres_auteur]  # Liste en compréhension
        else:
            raise ValueError(f"❌ Aucun livre trouvé pour l'auteur {auteur}.")

    def afficher_livres(self):
        """Affiche tous les livres sous forme de liste"""
        livres_list = [f"{titre} - {auteur}" for titre, auteur in self.livres.items()]  # Liste en compréhension
        return livres_list if livres_list else "📚 Aucun livre disponible."

    def livres_disponibles(self):
        """Méthode à implémenter pour afficher les livres disponibles"""
        raise NotImplementedError("🔴 Cette méthode doit être implémentée dans une sous-classe.")
