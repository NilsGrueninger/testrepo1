# Geisterspiel
from random import randint
print("Geisterspiel")
mutig = True
score = 0
while mutig:
    geistertuer = randint(1, 3)
    print("Vor dir sind drei Türen")
    print("Hinter dir ist dein Geist")
    print("Welche Tür öfnest du?")
    tuer= input ("1, 2, 3")
    tuer_nummer = int(tuer)
    if tuer_nummer == geistertuer:
        print("GEIST!")
        mutig = False
    else:
        print("Kein Geist")
        print("Neues Zimmer")
        score = score + 1
    print("Lauf Weg!")
    print("Spiel vorbei. Deine Punkte:", score)





