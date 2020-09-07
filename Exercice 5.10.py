
commande_client = {
                    0 : { "nom" : "RTX_3070" , "prix" : 519 } ,
                    1 : { "nom" : "RTX 3080" , "prix" : 719 } ,
                    2 : { "nom" : "RTX 3090" , "prix" : 1519 } 
                }

print(commande_client[0]["prix"] + commande_client[1]["prix"] + commande_client[2]["prix"])

argent_client = 3000
print(f"Le client donne : { argent_client }")

monnaie = 3000 - 2757

rest = 243 % 10

print(f"La caisse vous rend : { monnaie }" )