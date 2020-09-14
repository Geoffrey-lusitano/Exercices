# CONSIGNES

# Ecrire un algorithme qui demande deux nombres à l’utilisateur et l’informe ensuite si le produit est négatif ou positif (on inclut cette fois le traitement du cas où le produit peut être nul). Attention toutefois, on ne doit pas calculer le produit !

# ALGO
# Variable ecrire nb 1 puis nb 2 a utilisateur
# si nb1 < 0 et que nb2 < 0
# afficher le nombre est positif
# si nb1 > 0 et que nb 2 > 0
# afficher le nombre est positif
# sinon 
# afficher le nombre est négatif


nombre_1 = input("ecrivez un nombre : ")

nombre_2 = input("ecrivez un second nombre : ")

if int(nombre_1) < 0 and int(nombre_2) < 0:
    print("Le produit est positif")
elif int(nombre_1) > 0 and int(nombre_2) > 0:
    print("Le produit est positif")
else:
    print("Le produit est négatif")