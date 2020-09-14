# CONSIGNES 

# Ecrivez un algorithme permettant, toujours sur le même principe, à l’utilisateur de saisir un nombre déterminé de valeurs. Le programme, une fois la saisie terminée, renvoie la plus grande valeur en précisant quelle position elle occupe dans le tableau. On prendra soin d’effectuer la saisie dans un premier temps, et la recherche de la plus grande valeur du tableau dans un second temps.

# vARIABLE A Nombre Ecrire ""

# Tableau
# Si i dans liste Variable A
    # ajouter dans Tableau Nombre 
# Variable B = Max de Tableau
# Ecrire Variable B 
# Ecrire Position tableau Variabel B 

nombre = int(input("saisisez un nombre de valeurs : "))
tab = []
for ii in range(nombre): 
    tab.append(int(input("Entrer la valeur :"))) 

resultat = max(tab)

print(resultat)
print(tab.index(resultat))