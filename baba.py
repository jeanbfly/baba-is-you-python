import sys
from Objects import *
from Plateau import *

jeu = Plateau("level/level0")
print(jeu)
jeu.findRules()

"""
tant que le jeu est perdant, 
on demande la direction à l'utilisateur,
on bouge,
on print le plateau
"""

while not jeu.is_win():
    
    input_dir = input("Déplacement: ")

    if input_dir == "d":
        jeu.move("right")
    elif input_dir == "z":
        jeu.move("up")
    elif input_dir == "q":
        jeu.move("left")
    elif input_dir == "s":
        jeu.move("down")

    print(jeu)

print("gagné")