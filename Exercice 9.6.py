# CONSIGNES
# 
#  Un des plus anciens systèmes de cryptographie (aisément déchiffrable) consiste à décaler les lettres d’un message
# pour le rendre illisible. Ainsi, les A deviennent des B, les B des C, etc. Ecrivez un algorithme qui demande une phrase
# à l’utilisateur et qui la code selon ce principe. Comme dans le cas précédent, le codage doit s’effectuer au niveau de
# la variable stockant la phrase, et pas seulement à l’écran.

# ALGO

# Variable A = Ecrire ""
# Variable B = ""
# Variable C = Dictionnaire
# Si i dans A :
    # B ajoyté C
# Afficher B 
phrase = input("Ecrivez un message : ")
code = ""
crypto = {"a":"b", "b":"c", "c":"d", "d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"," ":" "}
for i in phrase :
    code += crypto[i]
print(f"votre code est {code}")
