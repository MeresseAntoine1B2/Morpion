def afficher_grille(grille):
    """
    Fonction qui affiche le plateau de jeu
    :param grille: (dict) Un dictionnaire qui représente une grille de morpion
    """
    print("   0    1    2")
    for cle in grille:
        print(cle + str(grille[cle]))
