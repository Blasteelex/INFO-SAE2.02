from Partie1.Langages import tousmots


def defauto():
    alphabet = list(set(input("Entrez l'alphabet : ").split()))
    etats = list(set(int(e) for e in (input("Entrez les états : ").split())))
    transitions = []
    tn = int(input("Entrez le nombre de transitions : "))
    for i in range(tn):
        temp1 = int(input("Entrez les transitions (État 1) : "))
        temp2 = input("Entrez les transitions (Lettre) : ")
        temp3 = int(input("Entrez les transitions (État 2) : "))
        temp = [temp1, temp2, temp3]
        transitions.append(temp)
    I = list(set(int(i) for i in input("Entrez les états Initiaux : ").split()))
    F = list(set(int(f) for f in input("Entrez les états Finaux : ").split()))

    automate = {
        "alphabet": alphabet,
        "etats": etats,
        "transitions": transitions,

        "I": I,
        "F": F
    }
    return automate

### test = defauto()

test = {
    "alphabet": ["a", "b", "c", "d"],
    "etats": [1, 2, 3, 4],
    "transitions": [
        [1, "a", 2],
        [1, "a", 4],
        [2, "b", 3],
        [4, "c", 3],
        [3, "d", 4]
    ],
    "I": [1],
    "F": [3, 4]
}



def lirelettre(T, E, a):
    accessibles = []
    for transition in T :
        if transition[0] in E and transition[1] == a :
            if transition[2] not in accessibles :
                accessibles.append(transition[2])
    return accessibles



def liremot(T, E, m):
    etats = E
    for lettre in m :
        etats = lirelettre(T, etats, lettre)
    return etats



def accepte(automate, m):
    etats = liremot(automate["transitions"], automate["I"], m)
    for etat in etats :
        if etat in automate["F"] :
            return True
    return False



def langage_accept(automate, n):
    mots = tousmots(automate["alphabet"], n-1)
    accept = []
    for m in mots:
        if accepte(automate, m):
            accept.append(m)
    return accept


# IL EST IMPOSSIBLE DE CRÉER UNE FONCTION QUI RENVOIE LE LANGAGE ACCEPTÉ CAR LE LANGAGE PEUT ÊTRE NON FINI,
# AINSI IL NE S'ARRÊTERA PAS DE TOURNER COMME L'ÉTOILE DE KLEENE.

if __name__ == "__main__" :

    print(test)

    print("Renvoie les états où l'on termine en lisant la lettre :")
    print(lirelettre(test["transitions"], test["etats"], "a"))

    print("Renvoie les états où l'on termine en lisant le mot :")
    print(liremot(test["transitions"], test["etats"], "ab"))

    print("Il est contraint de commencer au début :")
    print(lirelettre(test["transitions"], test["I"], "a"))

    print("Renvoie True si l'automate accepte le mot :")
    print(accepte(test, "ab"))
    print(accepte(test, "ac"))
    print(accepte(test, "abd"))
    print(accepte(test, "abdc"))

    print("Renvoie False si l'automate ne accepte pas le mot :")
    print(accepte(test, "abcd"))

    print("Mots acceptés de longueur < 3 :")
    print(langage_accept(test, 3))

    print(langage_accept(test, 10))