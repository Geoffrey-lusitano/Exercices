# CONSIGNES
# 
# Lire la suite des prix (en euros entiers et terminée par zéro) des achats d’un client. Calculer la somme qu’il doit, lire la somme qu’il paye, et simuler la remise de la monnaie en affichant les textes "10 Euros", "5 Euros" et "1 Euro" autant de fois qu’il y a de coupures de chaque sorte à rendre.
# 
#  Variable A dictionnaire avec liste des produits et prix
# Ecrire Variable A [O] + Variable A [1] + Variable A [2]
#  
# Variable B Ecrire Nombre "Quel somme allez vous donner ?"
# Variable C = Valeur absolue (Varialbe A - Variable B)
# Variable D = Variable C modulo 10
# Variable E = Variable D modulo 5
# Variable F = Variable C // 10
# Variable G = Variable D // 5
# Variable I = Variable E // 1 + 1 

# Si Varible C > Variable F : 
    # Ecrire Varible F 
    # Ecrire Variable G 
    # Ecrire Variable I

commande_client = {
                    0 : { "nom" : "RTX_3070" , "prix" : 519 } ,
                    1 : { "nom" : "RTX 3080" , "prix" : 719 } ,
                    2 : { "nom" : "RTX 3090" , "prix" : 1519 } 
                }

print(f"la somme due est de" , commande_client[0]["prix"] + commande_client[1]["prix"] + commande_client[2]["prix"])

argent_client = int(input("quel somme allez vous donner pour payer ? "))
print(f"Le client donne : { argent_client }")

monnaie_un = abs(argent_client - 2757)
monnaie_deux = monnaie_un % 10
monnaie_trois = monnaie_deux % 5
billet_dix = monnaie_un // 10
billet_cinq = monnaie_deux // 5
piece = (monnaie_trois // 1) + 1
if monnaie_un > billet_dix :
    print(f"la caisse vous rend {billet_dix} billet de 10 euros")
    print(f"la caisse vous rend {billet_cinq} billet de 5 euros")
    print(f"la caisse vous rend {piece} piece de 1 euro")
# print(f"La caisse ne rend pas la monnaie payer par carte ou vous perdrez: { monnaie_un }" )
# print(monnaie_deux)
# print(monnaie_trois)
# print(billet_cinq)
# print(piece)