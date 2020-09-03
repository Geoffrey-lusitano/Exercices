nombre_1 = input("ecrivez un nombre : ")

nombre_2 = input("ecrivez un second nombre : ")

if int(nombre_1) < 0 and int(nombre_2) < 0:
    print("Le produit est positif")
elif int(nombre_1) > 0 and int(nombre_2) > 0:
    print("Le produit est positif")
else:
    print("Le produit est négatif")