import numpy as np
import matplotlib.pyplot as plt
arr = np.array([[1, 2, 3], [4, 5, 6]])

# affichage
print(arr)
# parcours par ligne
for x in arr:
 print(x)
# exemple 2
# parcours par élément
for x in arr:
 for y in x:
  print(y)
# exemple 3
# parcours par élément avec un itérateur
for x in np.nditer(arr):
 print(x)
# exemple 4
# parcours avec emplacement, avec t le tuple (indice_ligne, indice_colonne)et e l’élément
for t,e in np.ndenumerate(arr):
 print(t,e) 

arr = np.array([1, 2, 3, 4, 5, 6, 14])


def my_searchsorted(table : object, element: int )-> int:
    """
    Prend en paramètre un tableau numpy trié table et un entier element 
    et retourne l'indice où l'élément doit être inséré pour que le tableau reste trié.
    
    Args:
        table (np.ndarray): Un tableau numpy trié
        element (int): L'élément à insérer dans le tableau
        
    Returns:
        int: L'indice où l'élément doit être inséré
    """
    for i in range(len(table)):
        if table[i] >= element:
            return i
    return len(table)

def my_searchsorted_where(table : object, element: int )-> int:
    """
    Prend en paramètre un tableau numpy trié table et un entier element 
    et retourne l'indice où l'élément doit être inséré pour que le tableau reste trié.
    
    Args:
        table (np.ndarray): Un tableau numpy trié
        element (int): L'élément à insérer dans le tableau
        
    Returns:
        int: L'indice où l'élément doit être inséré
    """
    return np.where(table >= element)[0][0] if np.any(table >= element) else len(table)

x = np.where(arr==4)
print(x)#[3,5,6]

arr = np.array([1, 2, 3, 4, 5, 4, 4])
""""""
def my_where(table : object, valeur : int )-> list:
    """
    Prend en paramètre un tableau numpy table et une valeur valeur 
    et retourne une liste des indices où la valeur est trouvée dans le tableau.
    
    Args:
        table (np.ndarray): Un tableau numpy
        valeur (int): La valeur à rechercher dans le tableau
        
    Returns:
        list: Une liste des indices où la valeur est trouvée dans le tableau
    """
    indices = []
    for i in range(len(table)):
        if table[i] == valeur:
            indices.append(i)
    return indices
  
x = my_where(arr, 4)
print("Les indices de 4 sont :", x)

#arrT= np.array([1, 2, 3, 4, 5, 4, 4],[1, 2, 3, 4, 5, 4, 4])
def my_where2(table : object, valeur : int )-> list:
    """
    Prend en paramètre un tableau numpy table et une valeur valeur 
    et retourne une liste des indices où la valeur est trouvée dans le tableau.
    
    Args:
        table (np.ndarray): Un tableau numpy
        valeur (int): La valeur à rechercher dans le tableau
        
    Returns:
        list: Une liste des indices où la valeur est trouvée dans le tableau
    """
    return [i for i in range(len(table)) if table[i] == valeur]

x = my_where2(arr, 4)
print("Les indices de 4 sont :", x)

arrT= np.array([[1, 2, 3, 4, 5, 4, 4],[1, 2, 3, 4, 5, 4, 4],[1, 2, 3, 4, 5, 4, 4]])
def my_where_multi(table : object, valeur : int )-> list:
    """
    Prend en paramètre un tableau numpy table et une valeur valeur 
    et retourne une liste des indices où la valeur est trouvée dans le tableau.
    
    Args:
        table (np.ndarray): Un tableau numpy
        valeur (int): La valeur à rechercher dans le tableau
        
    Returns:
        list: Une liste des indices où la valeur est trouvée dans le tableau
    """
    return [(i, j) 
            for i in range(table.shape[0]) 
            for j in range(table.shape[1]) 
            if table[i, j] == valeur]

x = my_where_multi(arrT, 4)
print("Les indices de 4 sont :", x)

# Ma fct add
def my_add(tableA : object, tableB : object)-> object:
    """
    Prend en paramètre deux tableaux numpy tableA et tableB 
    et retourne un nouveau tableau qui est la somme élément par élément des deux tableaux.
    
    Args:
        tableA (np.ndarray): Le premier tableau numpy
        tableB (np.ndarray): Le deuxième tableau numpy
        
    Returns:
        np.ndarray: Un nouveau tableau qui est la somme élément par élément des deux tableaux
    """
    if tableA.shape != tableB.shape:
        raise ValueError("Les tableaux doivent avoir la même forme pour l'addition.")
    
    result = np.empty(tableA.shape, dtype=tableA.dtype)
    for i in range(tableA.shape[0]):
        for j in range(tableA.shape[1]):
            result[i, j] = tableA[i, j] + tableB[i, j]
    return result

# Test de votre code
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
result = my_add(arr1, arr2)
print("La somme des deux tableaux est :\n", result)


def affiche_matrice(mat : object):
    """
    Prend en paramètre une matrice numpy mat et affiche son contenu de manière lisible.
    
    Args:
        mat (np.ndarray): La matrice numpy à afficher
    """
    print(mat)

# Test de votre code
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
affiche_matrice(mat)

def add_10(mat : object)-> object:
    """
    Prend en paramètre une matrice numpy mat et retourne une nouvelle matrice 
    où chaque élément est augmenté de 10.
    
    Args:
        mat (np.ndarray): La matrice numpy d'origine
        
    Returns:
        np.ndarray: Une nouvelle matrice avec chaque élément augmenté de 10
    """
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat[i, j] += 10
    return mat

# Test de votre code
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_mat = add_10(mat.copy())
print("La nouvelle matrice est :\n", new_mat)

def multiply_by_2(mat : object)-> object:
    """
    Prend en paramètre une matrice numpy mat et retourne une nouvelle matrice 
    où chaque élément est multiplié par 2.
    
    Args:
        mat (np.ndarray): La matrice numpy d'origine
        
    Returns:
        np.ndarray: Une nouvelle matrice avec chaque élément multiplié par 2
    """
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat[i, j] *= 2
    return mat
# Test de votre code
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_mat = multiply_by_2(mat.copy())
print("La latrice multiplié par 2 :\n", new_mat)

def show_2nd_line(mat : object):
    """
    Prend en paramètre une matrice numpy mat et affiche la deuxième ligne de cette matrice.
    
    Args:
        mat (np.ndarray): La matrice numpy
    """
    if mat.shape[0] < 2:
        raise ValueError("La matrice doit avoir au moins deux lignes.")
    
    print("La deuxième ligne de la matrice est :", mat[1])
# Test de votre code
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
show_2nd_line(mat)

def show_3rd_column(mat : object):
    """
    Prend en paramètre une matrice numpy mat et affiche la troisième colonne de cette matrice.
    
    Args:
        mat (np.ndarray): La matrice numpy
    """
    if mat.shape[1] < 3:
        raise ValueError("La matrice doit avoir au moins trois colonnes.")
    
    print("La troisième colonne de la matrice est :", mat[:, 2])

# Test de votre code
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
show_3rd_column(mat)

def extract_lil_matrix(mat : object)-> object:
    """
    Prend en paramètre une matrice numpy mat et retourne une nouvelle matrice 
    qui est la sous-matrice extraite des deux premières lignes et des deux premières colonnes de mat.
    
    Args:
        mat (np.ndarray): La matrice numpy d'origine
    Returns:
        np.ndarray: La sous-matrice extraite des deux premières lignes et des deux premières colon
    """
    if mat.shape[0] < 2 or mat.shape[1] < 2:
        raise ValueError("La matrice doit avoir au moins deux lignes et deux colonnes.")
    
    return mat[:2, :2]

# Test de votre code
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sub_mat = extract_lil_matrix(mat)
print("La sous-matrice extraite est :\n", sub_mat)
    
#Exercice 2
def random_matrix(int_nbr_of_line:int, int_nbr_of_column:int)-> object:
    """
    Prend en paramètre deux entiers int_nbr_of_line et int_nbr_of_column 
    et retourne une matrice numpy de dimensions (int_nbr_of_line, int_nbr_of_column) 
    remplie de nombres aléatoires entre 0 et 1.
    
    Args:
        int_nbr_of_line (int): Le nombre de lignes de la matrice
        int_nbr_of_column (int): Le nombre de colonnes de la matrice
        
    Returns:
        np.ndarray: Une matrice numpy remplie de nombres aléatoires entre 0 et 1
    """
    mat = np.empty((int_nbr_of_line, int_nbr_of_column))
    for i in range(int_nbr_of_line):
        for j in range(int_nbr_of_column):
            mat[i, j] = np.random.randint(1, 9)
    return mat

# Test de votre code
mat = random_matrix(4, 4)
print("La matrice aléatoire est :\n", mat)

def matrix_identity(int_nbr_of_line:int, int_nbr_of_column:int)-> object:
    """
    Prend en paramètre deux entiers int_nbr_of_line et int_nbr_of_column 
    et retourne une matrice identité numpy de dimensions (int_nbr_of_line, int_nbr_of_column).
    
    Args:
        int_nbr_of_line (int): Le nombre de lignes de la matrice
        int_nbr_of_column (int): Le nombre de colonnes de la matrice
        
    Returns:
        np.ndarray: Une matrice identité numpy
    """
    mat = np.zeros((int_nbr_of_line, int_nbr_of_column))
    for i in range(min(int_nbr_of_line, int_nbr_of_column)):
        mat[i, i] = 1
    return mat
# Test de votre code
mat = matrix_identity(4, 4)
print("La matrice identité est :\n", mat)

def function_matrix_trace(mat : object)-> int:
    """
    Prend en paramètre une matrice carrée numpy mat 
    et retourne la trace de cette matrice (la somme des éléments sur la diagonale principale).
    
    Args:
        mat (np.ndarray): La matrice carrée numpy
        
    Returns:
        int: La trace de la matrice
    """
    if mat.shape[0] != mat.shape[1]:
        raise ValueError("La matrice doit être carrée pour calculer la trace.")
    
    trace = 0
    for i in range(mat.shape[0]):
        trace += mat[i, i]
    return trace
# Test de votre code
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
trace = function_matrix_trace(mat)
print("La trace de la matrice est :", trace)

def matrice_adjacente(S,A):
    """_summary_

    Args:
        S (_type_): lst_sommets
        A (_type_): lst_aretes
    """
    
    





def multiply_matrices(matA : object, matB : object)-> object:
    """
    Prend en paramètre deux matrices numpy matA et matB 
    et retourne une nouvelle matrice qui est le produit matriciel de matA et matB.
    
    Args:
        matA (np.ndarray): La première matrice numpy
        matB (np.ndarray): La deuxième matrice numpy
        
    Returns:
        np.ndarray: Le produit matriciel de matA et matB
    """
    for i in range(matA.shape[0]):
        for j in range(matB.shape[1]):
            sum_product = 0
            for k in range(matA.shape[1]):
                sum_product += matA[i, k] * matB[k, j]
            matA[i, j] = sum_product
    return matA

# Test de votre code
matA = np.array([[1, 2], [3, 4]])
matB = np.array([[5, 6], [7, 8]])
product = multiply_matrices(matA.copy(), matB)
print("Le produit matriciel est :\n", product)
