# utiliser le module random pour genere un nombre aléatoire
# creer une valeur aleatoire
# créer une valeur de depart 
# boucle valeur de depart different de valeur aleatoire 
# faire ecrire un nombre a l utilisateur


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
