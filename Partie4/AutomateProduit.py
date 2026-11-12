from Partie4.entrepôt3 import *
from Partie2.Determinisation import *
from Partie3.Complementation import *

def inter(Automate1, Automate2) :

    if not deterministe(Automate1) : Automate1 = renommage(determinise(Automate1)) # Déterminiser ces automates est un gain de temps considérable,
    if not deterministe(Automate2) : Automate2 = renommage(determinise(Automate2)) # De fait ça optimise énormément la logique et la rapidité du programme.

    alphabet_produit = list(set(Automate1["alphabet"]) & set(Automate2["alphabet"]))

    etat_initial = (Automate1["I"][0], Automate2["I"][0])

    file_attente = [etat_initial]
    etats_produit = [etat_initial]
    transitions_produit = []

    while len(file_attente) > 0 :
        etat1, etat2 = file_attente.pop(0)

        for lettre in alphabet_produit :
            cible1 = lirelettre(Automate1["transitions"], [etat1], lettre )
            cible2 = lirelettre(Automate2["transitions"], [etat2], lettre )

            if cible1 and cible2 : # Vous l'aurez remarqué le code est similaire à la determinisation,
                # La boucle du procédé suit la même logique, de plus ici on revérifie avec les cibles que l'état ne soit pas mort.
                # Ainsi si l'un des états ne mène nulle part on ne crée pas de nouvel état produit.
                etat_produit_accessible = (cible1[0], cible2[0]) # L'automate est déterministe donc on prendra toujours le seul état où ça nous mène.
                transitions_produit.append([(etat1, etat2), lettre, etat_produit_accessible])
                if etat_produit_accessible not in etats_produit :
                    file_attente.append(etat_produit_accessible)
                    etats_produit.append(etat_produit_accessible)

    finaux = []
    for (etat1, etat2) in etats_produit :
        if etat1 in Automate1["F"] and etat2 in Automate2["F"] :
            finaux.append((etat1, etat2))


    return {
        "alphabet": alphabet_produit,
        "etats": etats_produit,
        "transitions": transitions_produit,
        "I": [etat_initial],
        "F": finaux
    }


def difference(Automate1, Automate2) :

    alphabet_different = Automate1["alphabet"]

    if not deterministe(Automate1) : Automate1 = renommage(determinise(Automate1))
    if not complet(Automate1) : Automate1 = complete( Automate1)

    Automate2["alphabet"] = list(set(Automate2["alphabet"]) | set(Automate1["alphabet"])) # On doit s'assurer que l'Automate 2 possède les lettres du 1
    if not deterministe(Automate2) : Automate2 = renommage(determinise(Automate2))
    if not complet(Automate2) : Automate2 = complete( Automate2)

    # Par définition, on veut qu'il soit complet, cependant, pour des raisons pratiques on va aussi le déterminiser.
    # Cela nous permettra également de réutiliser le code de la fonction inter.

    etat_initial = (Automate1["I"][0], Automate2["I"][0])

    file_differente = [etat_initial]
    etats_different = [etat_initial]
    transitions_differentes = [] 

    while len(file_differente) > 0 : 
        etat1, etat2 = file_differente.pop(0)
 
        for lettre in alphabet_different :
            cible1 = lirelettre(Automate1["transitions"], [etat1], lettre )
            cible2 = lirelettre(Automate2["transitions"], [etat2], lettre )

            if cible1 and cible2 :

                etat_different_accessible = (cible1[0], cible2[0])
                transitions_differentes.append([(etat1, etat2), lettre, etat_different_accessible])
                if etat_different_accessible not in etats_different :
                    file_differente.append(etat_different_accessible)
                    etats_different.append(etat_different_accessible)

    finaux = []
    for (etat1, etat2) in etats_different :
        if etat1 in Automate1["F"] and etat2 not in Automate2["F"] :
            finaux.append((etat1, etat2))


    return {
        "alphabet": alphabet_different,
        "etats": etats_different,
        "transitions": transitions_differentes,
        "I": [etat_initial],
        "F": finaux
    }


if __name__ == "__main__" :
    # print(inter(auto4,auto5))
    # print(renommage(inter(auto4,auto5)))
    #
    # print("")
    # print(difference(auto4,auto5))
    # print(renommage(difference(auto4,auto5)))
    #
    # print("")
    # print("")
    # print(inter(test_complet,test_incomplet))
    # print(renommage(inter(test_complet,test_incomplet)))
    #
    # print("")
    # print(difference(test_complet,test_incomplet))
    # print(renommage(difference(test_complet,test_incomplet)))

    print(inter(soutenance2, soutenance3))
    print(renommage(inter(soutenance2, soutenance3)))