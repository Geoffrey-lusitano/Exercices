
age = int(input("Quel age avez vous :"))
duree_permis = int(input("Ecrivez depuis combien de temps avez vous votre permis :"))
accident = int(input("Ecrivez le nombre d'accident responsable : "))

if age < 25 and duree_permis < 2:
    if accident == 0:
        print("Vous avez droit au tarif rouge")
    else:
        print("Nous ne pouvons pas vous assurer")
elif age < 25 and (duree_permis > 2 or age > 25):
    if accident == 0:
        print("Vous avez droit au tarif orange")
    elif accident == 1:
        print("Vous avez droit au tarif rouge")
    else:
        print("Nous ne pouvons pas vous assurer")
elif age > 25 and duree_permis > 2:
    if accident == 0:
        print("Vous avez droit au tarif vert")
    elif accident == 1:
        print("Vous avez droit au tarif orange")
    elif accident == 2:
        print("Vous avez droit au tarif rouge")
    else:
        print("Nous ne pouvons pas vous assurer")
else:
    pass

age_contrat = int(input("Si vous etes deja en contrat chez nous, depuis combien de temps : "))
if age_contrat > 5:
    input("Votre couleur d'assurance actuel : ")
    if "vert" or "Vert":
        print("Votre nouvelle couleur d'assurance est Bleu")
    elif "orange" or "Orange":
        print("Votre nouvelle couleur d'assurance est Vert")
    elif "rouge" or "Rouge":
        print("votre nouvelle couleur d'assurance est Orange")
    else:
        pass







    



