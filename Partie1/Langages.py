def concatene(L1, L2):
    concatenes = []
    for mot1 in L1:
        for mot2 in L2 :
            temp = mot1 + mot2 # Une concaténation de chaînes se fait avec + en .py.
            if temp not in concatenes:
                concatenes.append(temp)
    return concatenes

L1=['aa','ab','ba','bb']
L2=['a', 'b', '']



def puis(L, n):
    chaine = [""]
    for i in range(n):
        chaine = concatene(chaine, L)
    return chaine



# IL EST IMPOSSIBLE DE FAIRE DE FONCTION CALCULANT L'ÉTOILE D'UN LANGAGE
# L'ETOILE EST NON FINIE, EN L'OCCURENCE, L^100 PAR EX EST FINI ET MEME SI C'EST LONG ON PEUT L'ECRIRE,
# L^* EST INFINI ON NE RETOURNERA JAMAIS AUCUNE VALEUR CAR L'ETOILE S'INCRÉMENTE À L'INFINI.

def tousmots(L, n):
    nchaine = [""]
    if n == 0:
        return nchaine
    nliste = []
    for i in range(1, n + 1):
        nchaine = puis(L, i)
        for mot in nchaine:
            nliste.append(mot)
    nliste.append("") # C'est A* donc on ajoute le mot vide à la fin.
    return nliste



if __name__ == "__main__" :

    print( concatene(L1,L2))

    print( puis(L1, 2))

    print(tousmots(['a','b'],3))