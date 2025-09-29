from math import *

# Exercice 1

def moyenne_dune_lst(maliste: list) -> float:
    """Calculer la moyenne des valeurs d'une liste.

    Args:
        maliste (list): Liste de nombres.

    Returns:
        float: Moyenne des valeurs si la liste n'est pas vide.
        str: "Pas de notes" si la liste est vide.
    """
    moyenne = 0
    if not maliste:
        return "Pas de notes"
    for i in maliste:
        moyenne += i
    return moyenne / len(maliste)


def nb_sup(maliste: list[int], element: int) -> int:
    """Compter le nombre de valeurs strictement supérieures à un élément donné.

    Args:
        maliste (list[int]): Liste de nombres.
        element (int): Valeur de référence.

    Returns:
        int: Nombre d'éléments supérieurs à `element`.
        str: "Pas de liste" si la liste est vide.
    """
    occurences = 0
    if not maliste:
        return "Pas de liste"
    for i in maliste:
        if i > element:
            occurences += 1
    return occurences


def moy_sup(maliste: list, elt: int) -> float:
    """Calculer la moyenne des valeurs strictement supérieures à un élément.

    Args:
        maliste (list): Liste de nombres.
        elt (int): Valeur seuil.

    Returns:
        float: Moyenne des valeurs supérieures à `elt`.
        int: 0 si aucune valeur ne dépasse `elt`.
        str: "Pas de liste" si la liste est vide.
    """
    Lmoy = 0
    if not maliste:
        return "Pas de liste"
    Loccur = 0
    for i in maliste:
        if i > elt:
            Lmoy += i
            Loccur += 1
    return Lmoy / Loccur if Loccur > 0 else 0


def val_max(lst: list) -> float:
    """Trouver la valeur maximale d'une liste.

    Args:
        lst (list): Liste de nombres.

    Returns:
        float: Valeur maximale.
        str: "Pas de liste" si la liste est vide.
    """
    if not lst:
        return "Pas de liste"
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val


def ind_max(lst: list) -> int:
    """Donner l'indice de l'élément maximum dans une liste.

    Args:
        lst (list): Liste de nombres.

    Returns:
        int: Indice de l'élément maximal.
        str: "Pas de liste" si la liste est vide.
    """
    ind = 0
    if not lst:
        return "Pas de liste"
    max_val = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            ind = i
    return ind


# Exercice 2

def position(lst: list, elt: int) -> int:
    """Donner la position de la première occurrence d'un élément.

    Args:
        lst (list): Liste de nombres.
        elt (int): Élément recherché.

    Returns:
        int: Indice de la première occurrence.
        str: "Pas de liste" si la liste est vide.
    """
    if not lst:
        return "Pas de liste"
    for i in range(len(lst)):
        if lst[i] == elt:
            return i


def occurrences(lst: list, elt: int) -> int:
    """Compter le nombre d'occurrences d'un élément.

    Args:
        lst (list): Liste de nombres.
        elt (int): Élément à compter.

    Returns:
        int: Nombre d'occurrences.
        str: "Pas de liste" si la liste est vide.
    """
    if not lst:
        return "Pas de liste"
    occ = 0
    for i in lst:
        if i == elt:
            occ += 1
    return occ


# Exercice 3

def separer(lst: list[int]) -> list:
    """Réorganiser une liste en plaçant les négatifs au début,
    les zéros au milieu et les positifs à la fin.

    Args:
        lst (list[int]): Liste de nombres.

    Returns:
        list: Liste réorganisée.
        str: "Pas de liste" si la liste est vide.
    """
    lsep = []
    nbneg = 0
    if not lst:
        return "Pas de liste"
    for i in lst:
        if i < 0:
            lsep.insert(0, i)
            nbneg += 1
        elif i > 0:
            lsep.insert(-1, i)
        else:
            lsep.insert(nbneg, i)
    return lsep


# Exercice 4

def fizzbuzz(n: int) -> str:
    """Afficher la séquence FizzBuzz jusqu'à n.

    - Multiplies de 3 -> "Fizz"
    - Multiplies de 4 -> "Buzz"
    - Multiplies des deux -> "FizzBuzz"

    Args:
        n (int): Nombre limite (positif).

    Returns:
        None: Affiche directement le résultat.
        str: "Nombre positif uniquement" si `n` est négatif.
    """
    res=""
    if n < 0:
        return "Nombre positif uniquement"
    for i in range(1, n + 1):
        a = ""
        if i % 3 == 0:
            a += "Fizz"
        if i % 4 == 0:
            a += "Buzz"
        res+=str(i)+" : "+str(a)+"\n"
    return res


# Exercice 5

def convertir_argent(montant: float) -> dict:
    """Convertir un montant en billets/pièces disponibles.

    Args:
        montant (float): Montant en euros.

    Returns:
        dict: Dictionnaire {valeur: nombre d'occurrences}.
    """
    billets = [500, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]
    rendu = {}
    for b in billets:
        nb = int(montant // b)
        if nb > 0:
            rendu[b] = nb
            montant = round(montant - nb * b, 2)
    return rendu


# Exercice 6

def agencement(nbemplacement: int, lobjets: list) -> tuple:
    """Répartir des objets dans deux vitrines.

    Args:
        nbemplacement (int): Nombre maximal d'emplacements par vitrine.
        lobjets (list): Liste d'objets.

    Returns:
        tuple: Deux listes représentant les vitrines.
    """
    Lvitrine1 = []
    nbemplacement1 = 0
    Lvitrine2 = []
    nbemplacement2 = 0
    for i in range(len(lobjets)):
        if lobjets[i] not in Lvitrine1 and nbemplacement1 < 4:
            Lvitrine1.append(lobjets[i])
            nbemplacement1 += 1
        elif lobjets[i] not in Lvitrine2 and nbemplacement2 < 4:
            Lvitrine2.append(lobjets[i])
            nbemplacement2 += 1
    return Lvitrine1, Lvitrine2


# Exercice 9

def polynome(lst: list) -> float:
    """Évaluer un polynôme avec des coefficients donnés.

    Args:
        lst (list): Liste des coefficients.

    Returns:
        float: Résultat de l'évaluation.
    """
    resultat = 0
    puissance = len(lst)
    for i in range(len(lst)):
        resultat += lst[i] ** puissance
        puissance -= 1
    return resultat


def polynome2(lst: list, x: int) -> float:
    """Évaluer un polynôme en fonction d'une valeur x.

    Args:
        lst (list): Liste des coefficients.
        x (int): Valeur de la variable.

    Returns:
        float: Résultat du polynôme.
    """
    resultat = 0
    puissance = len(lst)
    for i in range(len(lst)):
        resultat += lst[i] ** puissance * x
        puissance -= 1
    return resultat



def main():
    L=[1,2,3,4,5,6,7]
    L1=[]
    L2=[0,0,0,0,0]
    L3=[8,9,0,7,6,4,8]
    """print(moyenne_dune_lst(L))
    print(moyenne_dune_lst(L1))
    print(moyenne_dune_lst(L2))
    print(moyenne_dune_lst(L3))
    print(nb_sup(L,4))
    print(nb_sup(L1,0))
    print(nb_sup(L2,8))
    print(nb_sup(L3,2))
    print(moy_sup(L,3))
    print(moy_sup(L1,0))
    print(moy_sup(L2,8))
    print(moy_sup(L3,2))
    print(val_max(L))
    print(val_max(L1))
    print(val_max(L2))
    print(val_max(L3))
    print(ind_max(L))
    print(ind_max(L1))
    print(ind_max(L2))
    print(ind_max(L3))
    print(separer([1,0,3,-4,5,0,9,-8]))
    print(separer([0,0,0,0,0,0]))
    print(separer([-2,-7,-5,8]))
    print(fizzbuzz(0))
    print(fizzbuzz(1))"""
    print(fizzbuzz(12))
    """print(fizzbuzz(-5))
    print(convertir_argent(0))
    print(convertir_argent(1))
    print(convertir_argent(50))
    print(convertir_argent(37))
    print(convertir_argent(700))
    print(agencement(4,[1,2,2,3,4,5,5]))
    print(agencement(7,[1,2,3,4,5]))
    print(agencement(0,[1,2,2,3,4,5,5]))
    print(agencement(1,[1]))
    print(polynome([3,4,5,7]))
    print(polynome([3,4,5,7]))
    print(polynome([3,4,5,7]))
    print(polynome([3,4,5,7]))
    print(polynome2([3,4,5,7],4))
    print(polynome2([3,4,5,7],4))
    print(polynome2([3,4,5,7],4))
    print(polynome2([3,4,5,7],4))"""

if __name__ =="__main__":
    main()
    
        
        



















            