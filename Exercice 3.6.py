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
