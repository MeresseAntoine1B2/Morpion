def afficher_grille(grille):
    """
    Fonction qui affiche le plateau de jeu
    :param grille: (dict) Un dictionnaire qui représente une grille de morpion
    """
    print("   0    1    2")
    for cle in grille:
        print(cle + str(grille[cle]))

def jouer_coup(grille:dict, joueur:str, coup:str):
    """
    Fonction qui joue un coup sur la grille
    :param grille: (dict) Un dictionnaire qui représente une grille de morpion
    :param joueur: (str) une chaine de caractères qui contient O ou X
    :param coup: (str) une chaine de caractères qui contient une lettre entre A et C en première position, et un chiffre entre 0 et 2 en seconde position
    :return: (Boolean) True si le coup est valide, false sinon
    """
    if coup[0] in ["A", "B", "C"] and 0 <= int(coup[1]) <= 2:
        if grille[coup[0]][int(coup[1])] == "-":
            grille[coup[0]][int(coup[1])] = joueur
            return True
    return False

def fonction_test():
    pass