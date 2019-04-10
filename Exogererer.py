#Entrez un nombre entre 0 & 9
from random import *
r = randint(0,9)
a = input( " entrez un nombre entre 0 et 9 : ")
#Si n = a, vous avez trouvé
if r == a:
    print("Félicitation")
#Sinon vous avez faussé
else:    
    print("Dommage mais recommence")