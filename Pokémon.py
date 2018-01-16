

elige_pokemon = input("Escoge a tu enemigo(Bulbasur,Charmander,Squirtle): ")

vida_pikachu = 100
vida_malo = 0

if elige_pokemon == "Bulbasur":
    vida_malo = 150

elif elige_pokemon == "Charmander":
    vida_malo = 130

elif elige_pokemon == "Squirtle":
    vida_malo = 140

while vida_pikachu >= 0 and vida_malo >= 0:
    elige_ataque = input("¿Como atacas a {} ? (Chispazo, Voltio):" .format(elige_pokemon))

    if elige_ataque == "Chispazo":
        vida_malo -= 30
    elif elige_ataque == "Voltio":
        vida_malo -= 25

    print("La vida del enemigo es de {}".format(vida_malo))

    if elige_pokemon == "Bulbasur":
        print("Squirtle te hizo 8 de daño")
        vida_pikachu -= 8
    elif elige_pokemon == "Charmander":
        print("Charmander te hizo 7 de daño")
        vida_pikachu -= 7
    elif elige_pokemon == "Squirtle":
        print("Bulbasur te hizo 10 de daño")
        vida_pikachu -= 10

    print("La vida de Pikachu es de {}".format(vida_pikachu))
