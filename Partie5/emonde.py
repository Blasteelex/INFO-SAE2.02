from Partie2.Determinisation import *


def est_emonde(Automate):
    etats_accessibles = set(Automate["I"])
    file = list(Automate["I"])
    while file :
        etat = file.pop(0)
        for transition in Automate["transitions"] :
            if transition[0] == etat and transition[2] not in etats_accessibles :
                etats_accessibles.add(transition[2])
                file.append(transition[2])
    if len(etats_accessibles) != len(Automate["etats"]) :
        return False

    etats_coaccessibles = set(Automate["F"])
    file = list(Automate["F"])
    while file :
        etat = file.pop(0)
        for transition in Automate["transitions"] :
            if transition[2] == etat and transition[0] not in etats_coaccessibles :
                etats_coaccessibles.add(transition[0])
                file.append(transition[0])

    if len(etats_coaccessibles) != len(Automate["etats"]) :
        return False

    return True

def emonde(Automate):
     if est_emonde(Automate) :
         return Automate
     else  :
        etats_accessibles = set(Automate["I"])
        file = list(Automate["I"])
        while file :
            etat = file.pop(0)
            for transition in Automate["transitions"] :
                if transition[0] == etat and transition[2] not in etats_accessibles :
                    etats_accessibles.add(transition[2])
                    file.append(transition[2])

        etats_coaccessibles = set(Automate["F"])
        file = list(Automate["F"])
        while file :
            etat = file.pop(0)
            for transition in Automate["transitions"] :
                if transition[2] == etat and transition[0] not in etats_coaccessibles :
                    etats_coaccessibles.add(transition[0])
                    file.append(transition[0])

        etats_emondes = list(etats_accessibles & etats_coaccessibles)
        transitions_emondes = [t for t in Automate["transitions"] if t[0] in etats_emondes and t[2] in etats_emondes]
        finaux =  [f for f in Automate["F"] if f in etats_emondes]
        initiaux = [i for i in Automate["I"] if i in etats_emondes]

        return {
            "alphabet": Automate["alphabet"],
            "etats": etats_emondes,
            "transitions": transitions_emondes,
            "I": initiaux,
            "F": finaux
        }