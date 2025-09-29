import random
def mix_list(list_to_mix)->list:
    """
    Mélange les éléments d'une liste sans modifier la liste d'origine.
    Args:
        list_to_mix (list): La liste à mélanger
    Returns:
        list: Une nouvelle liste avec les éléments mélangés
    """
    list_to_mix = list_to_mix[:]  
    for i in range(len(list_to_mix)-1, 0, -1):
        j = random.randint(0, i)
        list_to_mix[i], list_to_mix[j] = list_to_mix[j], list_to_mix[i]
    return list_to_mix

# Test de votre code 
lst_sorted=[i for i in range(10)] 
print(lst_sorted) 
print('Liste triée de départ',lst_sorted) 
mixed_list=mix_list(lst_sorted) 
print('Liste mélangée obtenue',mixed_list) 
print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted) 
#assert (cf. doc en ligne) permet de vérifier qu’une condition  
#est vérifiée en mode debug (désactivable) 
assert lst_sorted != mixed_list,"Les deux listes doivent être différente après l'appel à mixList.."

def choose_element_list(list_in_which_to_choose):
    """
    Prend en paramètre une liste list_in_which_to_choose de n'importe quoi 
    et retourne un élément de cette liste choisi au hasard.
    La liste de départ ne doit pas être modifiée lors de l'appel de la fonction.
    
    Args:
        list_in_which_to_choose (list): La liste dans laquelle choisir un élément
        
    Returns:
        object: Un élément choisi aléatoirement dans la liste
    """
    if not list_in_which_to_choose:
        raise ValueError("La liste ne doit pas être vide.")
    i = random.randint(0, len(list_in_which_to_choose) - 1)
    return list_in_which_to_choose[i]


print('Liste triée de départ',lst_sorted) 
e1 = choose_element_list(lst_sorted) 
print('A la première exécution',e1,'a été sélectionné') 
e2 = choose_element_list(lst_sorted) 
print('A la deuxième exécution',e2,'a été sélectionné') 
assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"

#exercice 3

def extract_elements_list(list_in_which_to_choose,int_nbr_of_element_to_extract)->list:
    """
    Prend en paramètre une liste list_in_which_to_choose de n'importe quoi 
    et un entier int_nbr_of_element_to_extract et qui retourne une liste 
    d'éléments de cette liste choisis au hasard. 
    La liste de départ ne doit pas être modifiée lors de l'appel de la fonction.
    
    Args:
        list_in_which_to_choose (list): La liste dans laquelle choisir des éléments
        int_nbr_of_element_to_extract (int): Le nombre d'éléments à extraire
        
    Returns:
        list: Une liste d'éléments choisis aléatoirement dans la liste
    """
    if int_nbr_of_element_to_extract > len(list_in_which_to_choose):
        raise ValueError("Le nombre d'éléments à extraire ne peut pas être supérieur à la taille de la liste.")
    
    list_copy = list_in_which_to_choose[:]
    extracted_elements = []
    
    for _ in range(int_nbr_of_element_to_extract):
        i = random.randint(0, len(list_copy) - 1)
        extracted_elements.append(list_copy[i])
        list_copy.pop(i)
    
    return extracted_elements

# Test de votre code 
print('Liste de départ',lst_sorted) 
sublist = extract_elements_list(lst_sorted,5) 
print('La sous liste extraite est',sublist) 
print('Liste de départ après appel de la fonction est',lst_sorted)

#exercice 6

def sort_list(list_to_sort)->list:
    """
    Trie une liste d'entiers en utilisant l'algorithme de tri à bulles.
    
    Args:
        list_to_sort (list): La liste d'entiers à trier
        
    Returns:
        list: La liste triée
    """
    n = len(list_to_sort)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort

# Test du code
lst_to_sort = [64, 34, 25, 12, 22, 11, 90]
print("Liste non triée :", lst_to_sort)
sorted_list = sort_list(lst_to_sort[:])  # Utiliser une copie pour préserver l'original
print("Liste triée :", sorted_list)
assert sorted_list == sorted(lst_to_sort), "Le tri n'a pas été effectué correctement."
