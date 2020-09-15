dictionnary = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

# print toutes les key du dictionnaire
print (dictionnary)
for x in dictionnary:
    print(x)
# print toutes les values
for x in dictionnary.values():
    print(x)
# boucler sur les cles et les valeurs
for x, y in dictionnary.items():
    print(x, y)
# regarder si une clé est présente dans le dictionnaire
if "brand" in dictionnary:
    print("Oui")
# ajouter un item
dictionnary["prix"] = 10000
print(dictionnary)
