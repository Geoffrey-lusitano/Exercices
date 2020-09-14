# CONSIGNES : 
# Ecrire un programme qui lit le prix HT d’un article, le nombre d’articles et le taux de TVA, et qui fournit le prix total TTC correspondant. Faire en sorte que des libellés apparaissent clairement.


# ALGO
# Varible article_prix en Numerique Ecrire "entrez le prix de l'article "
# Varible nombre_prix en Numerique Ecrire "entrez le nombre de l'article "

# variable tva
# calcul ( chiifre article_prix * nombre_article ) * chiffre a virgule (tva)
# afficher : "Le prix de l'article HT est de ", article_prix
# afficher "Il y a ", nombre_article, "dans votre panier."
# afficher "Le taux de TVA sur ces produits est de ", tva_taux
# afficher "Le prix TTC pour l'ensemble des produits est de ", prix_ttc


article_prix = input("donnez le prix de article :")

nombre_article = input("indiquez le nombre d'articles :")

tva_taux = (1.2)

prix_ttc = (int(article_prix)*int(nombre_article))*float(tva_taux)


print("Le prix de l'article HT est de ", article_prix)
print("Il y a ", nombre_article, "dans votre panier.")
print("Le taux de TVA sur ces produits est de ", tva_taux)
print("Le prix TTC pour l'ensemble des produits est de ", prix_ttc)
