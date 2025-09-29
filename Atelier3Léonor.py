import random

#Atelier 3 L3


#Exercice 1

def full_name(str_arg:str)->str:
    lst=str_arg.split()
    nom=lst[0].upper()
    prenom=lst[1].capitalize()
    return(nom+" "+prenom)
print(full_name("bisgamblia paul"))

#Exercice 2

def mots_Nlettres(lst_mot,n):
    L=[]
    for i in lst_mot:
        if len(i)==n:
            L.append(i)
    return L
    
def commence_par(mot,prefixe):
    return mot.split(prefixe)[0]==""

def finit_par(mot,suffixe):
    return mot.split(suffixe)[-1] == ''

print(commence_par("azerty","az"))

def finissent_par(lst_mot,suffixe):
    L=[]
    for i in lst_mot:
        if i.split(suffixe)[-1] == '':
            L.append(i)
    return L

def commencent_par(lst_mot,prefixe):
    L=[]
    for i in lst_mot:
        if i.split(prefixe)[-1] == '':
            L.append(i)
    return L

def liste_mots(lst_mot,prefixe,suffixe,n):
    L=finissent_par(lst_mot,suffixe)
    L1=commencent_par(L,prefixe)
    L2=mots_Nlettres(L1,n)
    return L2

def dictionnaire(fichier):
    with open('fichier', 'r') as file:
        for line in file:
            print(line.strip())
            
            
#Exercice 3

def place_lettre(ch:str,mot:str )->list:
    Lindices=[]
    for i in range(0,len(mot)):
        if mot[i]==ch:
            Lindices.append(i)
    return Lindices

print(place_lettre("m","maman"))

def demande_lettre():
    mot=str(input("Salut! Quel est ton mot ?"))
    place=str(input("Quelle lettre veux-tu connaître l'emplacement ?"))
    return "L'emplacement de ta lettre est à "+place_lettre(place,mot)+"de ton mot"

def outPutStr(mot:str,lpos:list)->str:
    newmot:str=""
    for i in range (0,len(mot)):
        if i not in lpos:
            newmot+="_"
        else:
            newmot+=mot[i]
    return newmot
            
print(outPutStr("bonjour",[0,1,4]))

def rungame(lst_mot:list):
    n=random.randint(1,len(lst_mot)-1)
    mot_choisi=lst_mot[n]
    mot_tirets=outPutStr(mot_choisi,[])
    nb_erreurs=0
    lst_lettres_trouvees=[]
    str_pendu=""
    while nb_erreurs<5:
        if "_" not in mot_tirets:
            print("Bravo vous avez gagné !")
            break     
        lettre_choisie=str(input("Devinez une lettre du mot !"))
        if len(lettre_choisie)==0 or len(lettre_choisie)>1:
            print("Aucune lettre ou plus d'une lettre n'est pas accepté, veuillez recommencer")
            continue
        elif len(place_lettre(lettre_choisie,mot_choisi))!=0:    
            lst_lettres_trouvees.append(lettre_choisie)
            # On récupère toutes les positions des lettres trouvées
            positions = []
            for lettre in lst_lettres_trouvees:
                positions += place_lettre(lettre, mot_choisi)
            mot_tirets = outPutStr(mot_choisi, positions)
            print(mot_tirets + "\n Bien joué ! Cette lettre était dans le mot \n")
        else:
            nb_erreurs+=1
            print("Eh non! La lettre choisie n'est pas dans le mot")
            match(nb_erreurs):
                case 5:
                    str_pendu+="|______\n+Perdu! le mot était"+mot_choisi
                case 4:
                    str_pendu+="|/ \ \n"
                case 3:
                    str_pendu+="| T \n"
                case 2:
                    str_pendu+="| O \n"
                case 1:
                    str_pendu+="|---] \n"
            print(str_pendu)
                    
lst =["paris","londres","madrid","berlin","new-york"]
rungame(lst)

#Exercice

def build_list(file_name: str) -> list:
    liste_pays_cap = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split('\t')
                if len(parts) == 2:
                    pays, capitale = parts
                    liste_pays_cap.append((pays, capitale))
    return liste_pays_cap

# Affichage du résultat
resultat = build_list("pays_capitales.txt")
print(resultat)


    
        
        
                    
                    
                
                
               
    
    
            
            
    
    




