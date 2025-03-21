from exercice_python.bibliotheque_en_ligne import BibliothequeEnLigne
from exercice_python.base_bibliotheque import BaseBibliotheque

if __name__ == '__main__':
    # ✅ Test des classes avec abstraction et héritage
    biblio_en_ligne = BibliothequeEnLigne()

    # Ajout de livres
    biblio_en_ligne.ajouter_livre("1984", "George Orwell")
    biblio_en_ligne.ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry")

    # Affichage des livres
    print("📚 Liste des livres :", biblio_en_ligne.afficher_livres())

    # Emprunt d'un livre
    biblio_en_ligne.emprunter_livre("1984", "Alice")

    # Vérification des livres disponibles
    print("📖 Livres disponibles :", biblio_en_ligne.livres_disponibles())

    # Rendre un livre
    biblio_en_ligne.rendre_livre("1984")

    # Vérification après retour
    print("📖 Livres disponibles après retour :", biblio_en_ligne.livres_disponibles())

    # Suppression d’un livre
    biblio_en_ligne.supprimer_livre("Le Petit Prince")

    # Tentative de suppression d’un livre inexistant
    try:
        biblio_en_ligne.supprimer_livre("Inconnu")
    except ValueError as e:
        print(e)

    # Utilisation de la méthode NotImplementedError
"""
   try:
        base = BaseBibliotheque()
        base.livres_disponibles()
    except NotImplementedError as e:
        print(f"🚨 Exception attendue : {e}")
"""
