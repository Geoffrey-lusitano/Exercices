# CONSIGNES

# Ecrire un algorithme qui choisit un nombre au hasard compris entre 1 et 100. Pour ceci, on utilise la fonction : iNombreHasard <- random[1..100] Demander à l'utilisateur de trouver le nombre. On fera apparaître un message : « Plus petit ! », et inversement, « Plus grand ! » jusqu’à ce que l'utilisateur ait trouvé et afficher en combien de coups.

# ALGO

# utiliser le module random pour genere un nombre aléatoire
# Variabel A valeur aleatoire
# Variable B valeur de depart 
# rep x 
# ecrie "quel est le nombre mystere"
    # Si pas nombre 
        # Ecrire Entrez un nombre valide
        # continuer
    # Si N > S :
        # Ecrire le nombre mystere est plus petit que S
    # si N < S :
        # Ecrire le nombre mystere est plus petit que S
        
# Variable C ecrire un nombre 


import random

n = random.randint(0, 100)
chance = 0

while chance != n :
    nombre = input( "Quel est le nombre mystère?" )
    if  not nombre.isdigit ():
        print( "SVP, entrez un nombre valide." )
        continue

    nombre = int(nombre)

    if  nombre  >  n :
        print(f"Le nombre mystère est plus petit que {nombre} ")
    elif  nombre  <  n :
        print(f"Le nombre mystère est plus grand que {nombre} ")
    else :
        print("Bravo, vous avez trouvé le nombre mystère!")
        exit ()
    chance += 1

print(f"Vous avez perdu. Le nombre mystère etait {n} ")
