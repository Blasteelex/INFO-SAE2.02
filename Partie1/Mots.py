def pref(mot):
    prefixes = []
    for i in range(0, len(mot) + 1):
        prefixes.append(mot[:i]) # Les slices permettent de couper un mot.
    return prefixes



def suf(mot):
    suffixes = []
    for i in range(0, len(mot) + 1):
        suffixes.append(mot[i:])
    return suffixes



def fact(mot):
    facteurs = []
    for i in range(0, len(mot) + 1):
        for j in range(i, len(mot) + 1):
            temp = mot[i:j] # La variable temp permet d'ajouter dans l'ordre les slices de fact.
            if temp not in facteurs: # Ici on évite les doublons sans passer par un set en désordre.
                facteurs.append(temp)
    return facteurs


def miroir(mot):
    return mot[::-1]



if __name__ == "__main__" :

    print(pref("coucou"))

    print(suf("coucou"))

    print(fact("coucou"))

    print(miroir("coucou"))