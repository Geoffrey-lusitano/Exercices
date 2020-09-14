# CONSIGNES 

# Ecrire un algorithme permettant de saisir 100 valeurs et qui les range au fur et à mesure dans un tableau. Cela s'appelle le tri à la volée (qui est une forme de tri par insertion)

# ALGO

# Variable A = 100
# Variable B = 0
# liste []
# Si Variable B <= Variable A :
    # Ajouter dans liste Nombre Ecrire ""
    # Variable B = + 1 chatour tour

nombre = 100
encore = 0
liste = []
while encore <= nombre  :
    liste.append(int(input("saisisez une valeurs : ")))
    encore += 1 