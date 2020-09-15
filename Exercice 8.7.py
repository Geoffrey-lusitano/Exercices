# Écrire un algorithme de jeu de dames très simplifié.
# L’ordinateur demande à l’utilisateur dans quelle case se trouve son pion (quelle ligne, quelle colonne). On met en
# place un contrôle de saisie afin de vérifier la validité des valeurs entrées.
# Ensuite, on demande à l’utilisateur quel mouvement il veut effectuer : 0 (en haut à gauche), 1 (en haut à droite), 2
# (en bas à gauche), 3 (en bas à droite).
# Si le mouvement est impossible (i.e. on sort du damier ), on le signale à l’utilisateur et on s’arrête là . Sinon, on
# déplace le pion et on affiche le damier résultant, en affichant un « O » pour une case vide et un « X » pour la case où
# se trouve le pion.

# ALGO



pion = int(input("Ou est votre pion ?"))

tableau = [] #Cette liste contiendra mon tableau en 2D
for i in range(10):
    tableau.append([0] * 10) #Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0
for i in tableau: 
    print(i)