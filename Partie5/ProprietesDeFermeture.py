from Partie1 import Automates
from Partie2.Determinisation import deterministe, renommage, determinise
from Partie5.entrepôt4 import *
from Partie5.emonde import est_emonde, emonde

def prefixe(Automate) :
    Automate= emonde(Automate)
    return {
        "alphabet": Automate["alphabet"],
        "etats": Automate["etats"],
        "transitions": Automate["transitions"],
        "I": Automate["I"],
        "F": list(Automate["etats"])
    }

def suffixe(Automate) :
    Automate= emonde(Automate)

    Automate = {
        "alphabet": Automate["alphabet"],
        "etats": Automate["etats"],
        "transitions": Automate["transitions"],
        "I": list(Automate["etats"]),
        "F": Automate["F"]
    }

    return renommage(determinise(Automate))


def facteur(Automate) :
    return suffixe(prefixe(Automate))

def miroir(Automate) :
    transitions_miroir = []
    for transition in Automate["transitions"] :
        transitions_miroir.append([transition[2], transition[1], transition[0]]) # On inverse simplement le sens.

    initiaux = list(Automate["F"])
    finaux = list(Automate["I"])

    Automate = {
        "alphabet": Automate["alphabet"],
        "etats": Automate["etats"],
        "transitions": transitions_miroir,
        "I": initiaux,
        "F": finaux
    }
    return determinise(emonde(Automate)) # Pour des raisons de complexité c'est plus
    # efficace d'émonder d'abord.

if __name__ == "__main__" :
    print(est_emonde(auto5))
    print(emonde(auto5))
    print(est_emonde(automate_pas_emonde))
    print((emonde(automate_pas_emonde)))
    print(prefixe(auto5))
    print(suffixe(auto5))
    print(facteur(auto5))

    print(prefixe(automate1))
    print(suffixe(automate1))
    print(facteur(automate1))
    automate2 = miroir(automate1)
    print(automate2)
    print(prefixe(automate2))
    print(suffixe(automate2))
    print(facteur(automate2))