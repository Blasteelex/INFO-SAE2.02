from operator import index

from Partie2.Determinisation import determinise, deterministe, renommage
from Partie3.entrepôt2 import *

def complet(Automate) :
    for etat in Automate["etats"] :
        for lettre in Automate["alphabet"] :
            temp = False
            for transition in Automate["transitions"] :
                if transition[0] == etat and transition[1] == lettre :
                    temp = True
                    break
            if not temp :
                return temp
    return True

def complete(Automate) :
    if complet(Automate) :
        return Automate
    Automate["etats"].append((Automate["etats"][-1])+1) # Je trouve que c'est l'approche la plus sûre, que l'on commence à 0 ou 1.
    puits = Automate["etats"][-1]

    for etat in Automate["etats"] : 
        temp = set()
        for transition in Automate["transitions"] :
            if transition[0] == etat :
                temp.add(transition[1])

        vers_puits = set(Automate["alphabet"]) - temp # Ici on récupère les lettres qui ne sont pas dans les transitions.

        for lettre in vers_puits :
            Automate["transitions"].append([etat, lettre, puits])

    return Automate


def complementaire(Automate):

    if not deterministe(Automate):
        Automate = renommage(determinise(Automate))

    if not complet(Automate):
        Automate = complete(Automate)

    finaux = []

    for etat in Automate["etats"]:
        if etat not in Automate["F"]:
            finaux.append(etat)

    Automate["F"] = finaux

    return Automate

if __name__ == "__main__" :
    print(complet(test_complet)) # Complet - True
    print(complet(test_incomplet)) # Incomplet - False

    print(" ")
    print(complet(test_incomplet))
    print(test_incomplet)
    print(complete(test_incomplet))
    print(complet(test_incomplet))

    print(" ")
    print(complementaire(test_complet)) # Par défaut déterministe complet on gagne du temps en ne traitant pas et on inverse.
    print(complementaire(test_incomplet)) # Ni complet ni déterministe on passe de 2 états à 5 d'ou la liste longue.

    print("")
    print(complementaire(test_incomplet_vaste)) # Bon c'était rapide... Mais la liste est longue... On a donc bien 0 1 2 3 5 6 le 4 était ["F"].