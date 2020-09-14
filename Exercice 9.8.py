# Ecrivez les algorithmes qui génèrent un Glup aléatoire tel que …
#  0 =< Glup =< 2
#  –1 =< Glup =< 1
#  1,35 =< Glup =< 1,65
#  Glup émule un dé à six faces
#  –10,5 =< Glup =< +6,5
#  Glup émule la somme du jet simultané de deux dés à six faces

import random

glub = random.randint(-1, 3)
glub2 = random.randint(-2, 2)
glub3 = random.uniform(1.34, 1.66)
glub4 = random.randint(1, 7)
glub5 = random.uniform(-10.4, 6.6)
glub6 = random.randint(0, 7) + random.randint(0, 7)

print(glub, glub2, glub3, glub4, glub5, glub6)