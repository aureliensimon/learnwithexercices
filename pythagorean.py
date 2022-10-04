import math
import time
 
z = input(" Si vous voulez calculer la longueur de l'hypoténuse tapez 1 ; si vous voulez savoir si le triangle est rectangle tapez 2  ;  ")
#Ceci inclus le fait que nous savons que le triangle est rectangle
if z == 1 :
   x = raw_input(" Nom du plus long coté  :  ")
   BC = input(" Longueur du deuxieme coté  :   ")
   AC = input(" Longueur du troisième coté  : ")
   time.sleep(1)
 
#Propiété
 
   print " D'après le théoreme de Pythagore on a : ",x,"au carré égal à la somme de ",BC," au carré et de ",AC,"au carré."
   time.sleep(2)
   print " Donc,",x," au carré est égal à ",BC**2,"plus",AC**2,"."
 
#Application
 
   print " Soit ",x,"au carré égal à ",BC**2+AC**2,"."
   time.sleep(2)
 
 
 
#Conclusion
 
print " Ainsi,",x," égale à la racinne carré de",BC**2+AC**2,"soit : "
print math.sqrt(BC**2+AC**2)
 
# On veut montrer que le triangle est rectangle
if z == 2 :
   x = input("Longueur du plus long coté  : ")
   BC = input(" Longueur du deuxieme coté :  ")
   AC = input(" Longueur du troisième coté : ")
   time.sleep(1)
   print " On compare ",x,"au carré à la somme de ",BC,"au carré et de",AC,"."
   print " On a : ",x," au caré égal à ",x**2,"."
   time.sleep(1)
   print " Et ",BC,"au carré plus ",AC,"au caré égal à ",BC**2,"plus",AC**2,"
   print "Soit : ",BC**2+AC**2,"."
 
if BC**2+AC**2 == x**2 :
   print " D'après la réciproque de Pythagore, le triangle est rectangle ."
 
elif BC**2+AC**2 != x**2 :
   print " D'après la contraposé du Théoreme de Pythagore, le triangle n'est pas rectangle ."