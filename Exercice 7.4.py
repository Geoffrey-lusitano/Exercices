# CONSIGNES

# Ecrivez un algorithme qui permette à l’utilisateur de supprimer une valeur d’un tableau préalablement saisi. L’utilisateur donnera l’indice de la valeur qu’il souhaite supprimer. Attention, il ne s’agit pas de remettre une valeur à zéro, mais bel et bien de la supprimer du tableau lui-même ! Si le tableau de départ était :
# 12
# 8
# 4
# 45
# 64
# 9
# 2
# Et que l’utilisateur souhaite supprimer la valeur d’indice 4, le nouveau tableau sera :
# 12
# 8
# 4
# 45
# 9
# 2

#  ALGO

# Liste = []
# Variable A = Nombre Ecrire ""
# Supprimer dans listes Variable A
# Afficher liste



liste = [4, 5, 6, 8, 7, 5]

element_a_supprimer = int(input("Entrez l'indice de la valeur a supprimer : "))
del liste[element_a_supprimer]

print(liste)