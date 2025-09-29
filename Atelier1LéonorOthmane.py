from math import sqrt

def message_imc(imc: float) -> str:
    """
    Retourne un message correspondant à l'indice de masse corporelle (IMC).

    Args:
        imc (float): L'indice de masse corporelle.

    Returns:
        str: Le message correspondant à la catégorie d'IMC.
    """
    seuils = [16.5, 18.5, 25, 30, 35, 40]
    messages = [
        'dénutrition ou famine',
        'maigreur',
        'corpulence normale',
        'surpoids',
        'obésité modérée',
        'obésité sévère',
        'obésité morbide'
    ]
    for i, seuil in enumerate(seuils):
        if imc < seuil:
            return messages[i]
    return messages[-1]


def est_bissextile(annee: int) -> bool:
    """
    Vérifie si une année est bissextile.

    Args:
        annee (int): L'année à vérifier.

    Returns:
        bool: True si l'année est bissextile, False sinon.
    """
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


def distance(xa: float, xb: float, ya: float, yb: float, za: float, zb: float) -> float:
    """
    Calcule la distance entre deux points dans un espace à trois dimensions.

    Args:
        xa, xb, ya, yb, za, zb (float): Coordonnées des points A et B.

    Returns:
        float: La distance entre les deux points.
    """
    return sqrt((xb - xa)**2 + (yb - ya)**2 + (zb - za)**2)


def inegal_triangle(a: float, b: float, c: float) -> bool:
    """
    Vérifie si trois longueurs peuvent former un triangle.

    Args:
        a, b, c (float): Longueurs des côtés.

    Returns:
        bool: True si les longueurs respectent l'inégalité triangulaire.
    """
    return a < b + c and b < a + c and c < a + b


def convertir_unite(x: int, dep: str, arr: str) -> int:
    """
    Convertit une masse d'une unité à une autre.

    Args:
        x (int): Valeur à convertir.
        dep (str): Unité de départ.
        arr (str): Unité d'arrivée.

    Returns:
        int: Valeur convertie.
    """
    unites = {'mg': 1, 'cg': 2, 'dg': 3, 'g': 4, 'dcg': 5, 'hg': 6, 'kg': 7}
    puissance = unites[dep] - unites[arr]
    return x * 10**puissance


def calculer_mes_impots(mon_revenu: int) -> float:
    """
    Calcule le montant des impôts en fonction du revenu.

    Args:
        mon_revenu (int): Revenu annuel en euros.

    Returns:
        float: Montant des impôts.
    """
    if mon_revenu > 180294:
        return mon_revenu * 0.45
    elif mon_revenu > 83824:
        return mon_revenu * 0.41
    elif mon_revenu > 29315:
        return mon_revenu * 0.30
    elif mon_revenu > 11498:
        return mon_revenu * 0.11
    else:
        return 0.0


if __name__ == "__main__":
    print(message_imc(41))
    print(message_imc(22))
    print(est_bissextile(2010))
    print(est_bissextile(2020))
    print(inegal_triangle(1, 3, 5))
    print(inegal_triangle(2, 2, 3))
    print(convertir_unite(45, 'kg', 'mg'))
    print("Votre revenu imposable est:", calculer_mes_impots(32000), "€")
