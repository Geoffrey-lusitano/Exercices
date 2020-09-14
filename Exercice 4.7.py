# CONSIGNES 

# Une compagnie d'assurance automobile propose à ses clients quatre familles de tarifs identifiables par une couleur, du moins au plus onéreux : tarifs bleu, vert, orange et rouge. Le tarif dépend de la situation du conducteur :
#  un conducteur de moins de 25 ans et titulaire du permis depuis moins de deux ans, se voit attribuer le tarif rouge, si toutefois il n'a jamais été responsable d'accident. Sinon, la compagnie refuse de l'assurer.
#  un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans, ou de plus de 25 ans mais titulaire du permis depuis moins de deux ans a le droit au tarif orange s'il n'a jamais provoqué d'accident, au tarif rouge pour un accident, sinon il est refusé.
#  un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun accident et du tarif orange pour un accident, du tarif rouge pour deux accidents, et refusé au-delà
#  De plus, pour encourager la fidélité des clients acceptés, la compagnie propose un contrat de la couleur immédiatement la plus avantageuse s'il est entré dans la maison depuis plus de cinq ans. Ainsi, s'il satisfait à cette exigence, un client normalement "vert" devient "bleu", un client normalement "orange" devient "vert", et le "rouge" devient orange.
# Ecrire l'algorithme permettant de saisir les données nécessaires (sans contrôle de saisie) et de traiter ce problème. Avant de se lancer à corps perdu dans cet exercice, on pourra réfléchir un peu et s'apercevoir qu'il est plus simple qu'il n'en a l'air (cela s'appelle faire une analyse !)


# ALGO

# Variable a Ecrire : l age de utilisateur
# Variable b Ecrire : cb d année de permis
# Variable c Ecrire : nombre d accident responsable
# si age < 25 et année de permis < 2
    #si accident == 0 
    # afficher vous avez droit au tarif rouge
    # sinon 
    # afficher nous ne pouvons pas vous assurer 

# demander duree du contrat chez assurareur si present
# si duree contrat > 5
    # demander la couleur d'assurance actuel
    # si vert:
        # afficher bleu





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







    



