from Partie1.Automates import lirelettre
from Partie2.entrepôt import *

def deterministe(Automate) :
    if len(Automate["I"]) != 1: # Un automate déterministe possède un seul état initial.
        return False

    for etat in Automate["etats"] :
        for lettre in Automate["alphabet"] :
            temp = lirelettre(Automate["transitions"], [etat], lettre) # l'état devient une liste temporaire qui change à chaque boucle.
            if len(temp) > 1 :
                return False
    return True

def determinise(Automate) :
    initial = sorted(list(set(Automate["I"])))
    file_attente = [initial]
    nouveaux_etats = [initial]
    nouvelles_transitions = []

    if deterministe(Automate) :
        return Automate
    while len(file_attente) > 0 :

        etat_attente = file_attente.pop(0)

        for lettre in Automate["alphabet"] :

            etats_cibles = lirelettre(Automate["transitions"], etat_attente, lettre)

            if etats_cibles : # On vérifie que l'état ne soit pas "mort", qu'il mène qq part.

                nouvel_etat = sorted(list(set(etats_cibles)))
                nouvelles_transitions.append([etat_attente, lettre, nouvel_etat])

                if nouvel_etat not in nouveaux_etats :
                    nouveaux_etats.append(nouvel_etat)
                    file_attente.append(nouvel_etat)

    finaux = []
    for ne in nouveaux_etats:
        for e in ne:
            if e in Automate["F"]:
                if ne not in finaux:
                    finaux.append(ne)
                break

    return {
        "alphabet": Automate["alphabet"],
        "I": [initial],
        "transitions": nouvelles_transitions,
        "etats": nouveaux_etats,
        "F": finaux
    }

def renommage(Automate) :
    indices = {}
    for indice, etat in enumerate(Automate["etats"]):
        indices[tuple(etat)] = indice # Les dicos ne prennent que des valeurs immuables.

    transitions = []
    for transition in Automate["transitions"] :
        transitions.append([indices[tuple(transition[0])], transition[1], indices[tuple(transition[2])]])

    etats = list(indices.values())

    finaux = []
    for etat in Automate["F"] :
        finaux.append(indices[tuple(etat)])

    return {
        "alphabet": Automate["alphabet"],
        "etats": etats,
        "transitions": transitions,
        "I": [0], # Par définition 0 sera toujours l'état initial car c'est le premier créé.
        "F": finaux
    }


if __name__ == "__main__" :
    # print(deterministe(test)) # False
    # print(deterministe(test2)) # False
    # print(deterministe(test3)) # True
    #
    # print("")
    #
    # print(test)
    # print(determinise(test))
    # print(renommage(determinise(test)))
    #
    # print("")
    #
    # print(auto2)
    # print(determinise(auto2))
    # print(renommage(determinise(auto2)))
    #
    # print("")
    # # Ici on montre l'effacité de la fonction determinise en testant avec déterministe.
    # print(test3) # Déterministe.
    # print(determinise(test3)) # Il doit renvoyer exactement l'automate donné sans le calculer.
    #

    print(determinise(soutenance1))
    print(renommage(determinise(soutenance1)))
