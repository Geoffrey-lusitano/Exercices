import math

nb_chevaux = int(input("entrez le nombre de chevaux : "))
nb_chevaux_parie = int(input("entrez le nombre de cheveux parié : "))

ordre = math.factorial(nb_chevaux)/ math.factorial(nb_chevaux - nb_chevaux_parie)
desordre = math.factorial(nb_chevaux) / math.factorial((math.factorial(nb_chevaux_parie)) * (nb_chevaux - nb_chevaux_parie))
print(f"ordre : {ordre}")
print(f"desordre : {desordre}")

