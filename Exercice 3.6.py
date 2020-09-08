# demander age enfant a l utilisateur
# si age_enfant == 6 ou == 7
# afficher catégorie poussin
# si age enfant == 8 ou 9 
# afficher catégorie pupille
# si age enfant == 10 ou 11
# afficher categorie minime
# si age enfant >= 12
# afficher categorie cadet
# sinon 
# affichier il n y as pas de catégories pour votre enfant




age_enfant = int(input("Ecrivez l'age de votre enfant : "))

if age_enfant == 6 or age_enfant == 7:
    print("Votre enfant est en Catégorie Poussin")
elif age_enfant == 8 or age_enfant == 9:
    print("Votre enfant est en catégorie Pupille")
elif age_enfant == 10 or age_enfant == 11:
    print("Votre enfant est en catégorie Minime")
elif age_enfant >= 12:
    print("Votre enfant est en catégorie Cadet")
else:
    print("Il n'y as pas de catégories pour votre enfant")
