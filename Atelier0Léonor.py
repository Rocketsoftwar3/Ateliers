import random
#Exercice Papier caillou ciseaux

# Liste des choix possibles
CHOIX = ['pierre', 'papier', 'ciseaux']


def demander_joueurs():
    """
    Initialise les noms des joueurs et le mode de jeu (1 joueur contre bot ou 2 joueurs).

    Returns:
        tuple: (nom_joueur1, nom_joueur2, mode_bot)
               mode_bot est True si le joueur affronte l'ordinateur, False sinon.
    """
    n1 = input("Quel est votre nom ? ")
    bot = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").upper()

    if bot == 'O':
        print(f"Bienvenue {n1}, nous allons jouer ensemble.")
        n2 = "Machine"
        return n1, n2, True

    elif bot == 'N':
        print(f"Bienvenue {n1}, nous allons jouer ensemble.")
        n2 = input("Quel est le nom du deuxième joueur ? ")
        print(f"Bienvenue {n2} !")
        return n1, n2, False

    else:
        print("Réponse non reconnue. Relancez le jeu et répondez par O ou N.")
        exit()


def choix_joueur(nom):
    """
    Demande à un joueur humain de faire un choix valide.

    Args:
        nom (str): Le nom du joueur.

    Returns:
        str: Le choix du joueur ('pierre', 'papier' ou 'ciseaux').
    """
    while True:
        choix = input(f"{nom}, faites votre choix (pierre, papier, ciseaux) : ").lower()
        if choix in CHOIX:
            return choix
        print("Choix invalide, réessayez.")


def choix_machine():
    """
    Génère un choix aléatoire pour la machine.

    Returns:
        str: Le choix de la machine.
    """
    return random.choice(CHOIX)


def jouer_manche(p1, p2):
    """
    Détermine le gagnant d'une manche.

    Args:
        p1 (str): choix du joueur 1.
        p2 (str): choix du joueur 2.

    Returns:
        int: 1 si joueur 1 gagne, 2 si joueur 2 gagne, 0 en cas d'égalité.
    """
    if p1 == p2:
        return 0

    if (p1 == 'pierre' and p2 == 'ciseaux') \
       or (p1 == 'ciseaux' and p2 == 'papier') \
       or (p1 == 'papier' and p2 == 'pierre'):
        return 1
    else:
        return 2


def boucle_principale():
    """
    Fonction principale qui gère les manches et les scores (maximum 5 parties).
    """
    n1, n2, contre_bot = demander_joueurs()
    score1 = 0
    score2 = 0
    parties = 0

    while parties < 5:
        # Récupérer les choix
        c1 = choix_joueur(n1)
        c2 = choix_machine() if contre_bot else choix_joueur(n2)

        # Afficher le choix de chaque joueur
        print(f"{n1} a choisi {c1} | {n2} a choisi {c2}")

        # Déterminer le gagnant
        resultat = jouer_manche(c1, c2)
        if resultat == 1:
            print(f"{n1} remporte cette manche !")
            score1 += 1
        elif resultat == 2:
            print(f"{n2} remporte cette manche !")
            score2 += 1
        else:
            print("Égalité !")

        # Afficher les scores
        print(f"Score : {n1} = {score1} | {n2} = {score2}")

        parties += 1

        # Demander si on continue
        if parties < 5:
            continuer = input("Voulez-vous refaire une partie ? (O/N) ").upper()
            if continuer != 'O':
                break

    print("Merci d'avoir joué, à bientôt !")


if __name__ == "__main__":
    boucle_principale()

#Exercice Code postal

verte={20:1.16,100:2.32,250:4.00,500:6.00,1000:7.50,3000:10.50}
prioritaire={20:1.43,100:2.86,250:5.26,500:7.89,3000:11.44}
ecopli={20:1.14,100:2.28,250:3.92}
L=['verte','prioritaire','ecopli']

def choixLettre():
    """L'utilisateur choisit le type de lettre qu'il veut envoyer ai
    nsi que son poids"""

    """tant que type est false, on demande à l'utilisateur de saisir
      un code valide et un poids en chiffre"""
    type=False
    while type==False:
        type_lettre=input("Précisez le type de lettre(verte,prioritaire,écopli)")
        poids_lettre=input("Précisez le poids de la lettre en grammes")
        if type_lettre in L and type(poids_lettre)==int :
            type=True
        prix=calculprix(type_lettre,poids_lettre)
        print(prix)

def calculprix(type_lettre,poids_lettre):
    """En fonction du type de lettre et de poids, calcule le prix"""

    """On identifie le type de lettre grâce à la première boucle for qui itère dans la
    liste des types"""

    for i in range(len(L)):
        if type_lettre==L[i]:
            type_lettre=L[i]
    type_lettre=eval(type_lettre)
    """transforme le type de type_lettres en simple variable"""

    L2=list(type_lettre.items())
    """On itère sur le dictionnaire pour identifier à quelle tranche de 
        prix correspond le poids"""
    
    for i,j in type_lettre.items():   
        if poids_lettre<=i:
            return j
        if poids_lettre>L2[-1][-1]:
            return "Poids trop grand",str(type_lettre),calculprix(type_lettre,poids_lettre)
    
        
choixLettre()        





