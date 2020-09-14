# CONSIGNES 

# Écrire un algorithme qui permette de connaître ses chances de gagner au tiercé, quarté, quinté et autres impôts volontaires.
# On demande à l’utilisateur le nombre de chevaux partants, et le nombre de chevaux joués. Les deux messages affichés devront être : Dans l’ordre : une chance sur X de gagner Dans le désordre : une chance sur Y de gagner
# X et Y nous sont donnés par la formule suivante, si n est le nombre de chevaux partants et p le nombre de chevaux joués (on rappelle que le signe ! signifie "factorielle", comme dans l'exercice 5.7 ci-dessus) : X = n ! / (n - p) ! Y = n ! / (p ! * (n – p) !)
# NB : cet algorithme peut être écrit d’une manière simple, mais relativement peu performante. Ses performances peuvent être singulièrement augmentées par une petite astuce. Vous commencerez par écrire la manière la plus simple, puis vous identifierez le problème, et écrirez une deuxième version permettant de le résoudre.

# ALGO

# iMPORTER METHODE math
# Variable A Ecrire Nombre "entrez nombre de chevaux"
# Variable B Ecrire Nombre "entrez nombre de chevaux pariée"

# Variable C = Factorial A / Factorial A - C
# Variable D = Factorial A / ........

# Afficher C 
# Affocher D 


import math

nb_chevaux = int(input("entrez le nombre de chevaux : "))
nb_chevaux_parie = int(input("entrez le nombre de cheveux parié : "))

ordre = math.factorial(nb_chevaux)/ math.factorial(nb_chevaux - nb_chevaux_parie)
desordre = math.factorial(nb_chevaux) / math.factorial((math.factorial(nb_chevaux_parie)) * (nb_chevaux - nb_chevaux_parie))
print(f"ordre : {ordre}")
print(f"desordre : {desordre}")

