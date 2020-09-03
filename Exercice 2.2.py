article_prix = input("donnez le prix de article :")

nombre_article = input("indiquez le nombre d'articles :")

tva_taux = (1.2)

prix_ttc = (int(article_prix)*int(nombre_article))*float(tva_taux)


print("Le prix de l'article HT est de ", article_prix)
print("Il y a ", nombre_article, "dans votre panier.")
print("Le taux de TVA sur ces produits est de ", tva_taux)
print("Le prix TTC pour l'ensemble des produits est de ", prix_ttc)
