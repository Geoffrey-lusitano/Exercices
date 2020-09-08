# faire une liste ou un dictionnaire avec 
# 
#

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