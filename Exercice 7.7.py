# CONSIGNES

# Écrivez un algorithme qui fusionne deux tableaux (déjà existants) dans un troisième, qui devra être trié.
# Attention ! On présume que les deux tableaux de départ sont préalablement triés : il est donc irrationnel de faire une simple concaténation des deux tableaux de départ, puis d'opérer un tri : comme quand on se trouve face à deux tas de papiers déjà triés et qu'on veut les réunir, il existe une méthode bien plus économique (et donc, bien plus rationnelle...)

# ALGO

# Liste A []
# Liste B []
# liste C []
# liste C = A + B 
# Liste C tri
# Afficher Liste C

liste_un = [6, 7, 8, 9]
liste_deux = [1, 2, 3, 4, 5]
liste_trois = []
liste_trois = liste_un + liste_deux
liste_trois.sort()
print(liste_trois)
