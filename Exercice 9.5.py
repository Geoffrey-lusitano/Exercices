# CONSIGNES 

# Ecrivez un algorithme qui demande une phrase à l’utilisateur. Celui-ci entrera ensuite le rang d’un caractère à
# supprimer, et la nouvelle phrase doit être affichée (on doit réellement supprimer le caractère dans la variable qui
# stocke la phrase, et pas uniquement à l’écran).

# ALGO

# Variable A Ecrire ""
# Afficher longueur A
# liste = [ i pour i dans A]
# Variable B = Nombre Ecrire ""
# Afficher B dans liste  
# Supprimer B dans liste 
# Variable C = "". ajouter liste
# Afficher C
phrase = input("Ecrivez une phrase svp : ")
print(len(phrase))
liste = [i for i in phrase]
s = int(input("Entrez l index a supprimer : "))
print(liste[s])

del liste[s]
phrase2 = "" .join(liste)
print(phrase2)