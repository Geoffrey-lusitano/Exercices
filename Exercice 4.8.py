# CONSIGNES 

# Ecrivez un algorithme qui a près avoir demandé un numéro de jour, de mois et d'année à l'utilisateur, renvoie s'il s'agit ou non d'une date valide.
# Cet exercice est certes d’un manque d’originalité affligeant, mais après tout, en algorithmique comme ailleurs, il faut connaître ses classiques ! Et quand on a fait cela une fois dans sa vie, on apprécie pleinement l’existence d’un type numérique « date » dans certains langages…).
# Il n'est sans doute pas inutile de rappeler rapidement que le mois de février compte 28 jours, sauf si l’année est bissextile, auquel cas il en compte 29. L’année est bissextile si elle est divisible par quatre. Toutefois, les années divisibles par 100 ne sont pas bissextiles, mais les années divisibles par 400 le sont.

# ALGO

# Variable A Ecrire de choisir un jour
# Variable B Ecrire de choisir un mois
# Variable C Ecrire de choisir une année

# variable bissextile = année modulo 4 == 0
# faire une liste avec les mois
# si n_mois == 2 
    # si (bissextile et mois = 2 et jours <= 29) ou (n'est pas bissextile et mois = 2 et jour <= 28)
        # afficher cette date est vailde
    # sinon :
        # afficher cette date n'est pas valide
# et si jour > 0 et jour <= liste de mois dans un mois
    # afficher cette date est valide
# sinon 
    # afficher cette date n'est pas valide


n_jour = int(input("Selectionner le jour souhaité"))
n_mois = int(input("Selectionner le mois souhaité"))
n_annee = int(input("Selectionner l'année'souhaitée"))

is_bissextile = n_annee%4 == 0

mois = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if n_mois == 2 :
    if (is_bissextile and n_mois == 2 and n_jour <= 29) or (not(is_bissextile) and n_mois == 2 and n_jour <= 28) :
        print("Cette date est valide")
    else :
        print("Cette date n'est pas valide")
elif n_jour > 0 and n_jour <= mois[n_mois] :
    print("Cette date est valide")
else :
    print("Cette date n'est pas valide")    




