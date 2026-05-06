#!/usr/bin/env python3

def pow(a, b):

    if b == 0:
        return 1
    elif b > 0:
        exposant = b
    else:
        exposant = -b
        # sert pour l'utilisation de la boucle
        # mais au final l'exposant reste positif
        # car -(-3) = 3
        # si on utilisait b à la place de exposant
        #  dans la boucle ci-dessous ça créerait une
        # erreur car la boucle ne prend pas en charge le négatif
        # ça voudrait dire parcourt i pendant -3 fois -> Pas possible

    result = 1
    for i in range(exposant):
        result = result * a

    if b < 0:
        return 1 / result
        # # b et pas exposant car on a besoin de b
        # pour savoir si b est négatif de base
    return result
