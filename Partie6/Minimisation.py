from turtledemo.sorting_animate import partition

from Partie2.Determinisation import deterministe, determinise
from Partie3.Complementation import complet, complete
from Partie6.entrepôt5 import automate_minimisation_cours, TueurDeProcesseur


def minimisation(Automate) :
    if not deterministe(Automate) :
        Automate = determinise(Automate) # On déterminise l'automate.'
    if not complet(Automate) :
        Automate = complete(Automate) # On le complète, puis on peut minimiser.

    classe = classes_equivalentes(Automate) # On récupère les classes équivalentes.
    classes = constructeur_classes(classe) # On en fait un dictionnaire ordonné.
    return constructeur_automate(Automate, classes) # On retourne le nouvel automate minimisé.

def table_de_transition(Automate) :
    table_de_transition = { }
    Automate["alphabet"] = sorted(Automate["alphabet"]) # C'est plus plaisant d'avoir les lettres dans l'ordre.

    for etat in Automate["etats"] :
        liste_transition = [] # Cette liste stocke la transition d'arrivée pour la lettre. a = 1 b = 2 c = 1
        for lettre in Automate["alphabet"] :
            for transition in Automate["transitions"] : # Ainsi pour chaque lettre on va chercher la transition correspondante.
                if transition[0] == etat and transition[1] == lettre :
                    liste_transition.append(transition[2])
                    break # On casse la boucle -> on associe le tuple (car les dicos n'acceptent pas les listes) à l'état testé.
        table_de_transition[etat] = tuple(liste_transition)

    return table_de_transition # On finit avec la table de transition correspondante
    # qui peut même se print, ce qui peut être sympa pour aider en cours.

def classes_equivalentes(Automate) :
    table_transitive = table_de_transition(Automate) # On récupère la table de transition.
    finaux = set(Automate["F"]) # On crée un ensemble de finaux.

    classe = {} # On initialise la classe de niveau 0.
    for etat in Automate["etats"] : # Ici, on gère la logique de la classe 0.
        if etat in finaux :
            classe[etat] = 1 # Si 1, c'est un final.
        else :
            classe[etat] = 0 # Si 0, c'est un autre.

    while True : # Cette boucle est délimitée par la fonction d'arrêt en dessous
        # Selon sa logique si la classe créée est similaire à celle d'avant on coupe, comme vu en cours.
        nouvelle_classe = {} # Ceci est donc la nouvelle classe.
        signatures = {} # Les signatures sont les tuples de la classe qui représentent la classe actuelle
        # Et la classe de destination de la lettre.
        prochaine_classe = 0 # Ce compteur permet de calculer les classes grâce au système de signature.

        for etat in Automate["etats"] :
            signature = [classe[etat]] # La signature est à l'origine la classe qu'on traite.
            for destination in table_transitive[etat] : # Pour chaque dest associée à la classe,
                # On ajoute sa destination, soit 1 ou 0 selon la classe d'avant.
                signature.append(classe[destination])
            signature = tuple(signature) # Encore une fois les dicos aiment les tuples, pas les listes.

            if signature not in signatures : # Là, c'est intéressant,
                # Dans le cas ou la signature n'a pas encore été trouvée, on a des cas différents,
                # Ainsi, on doit lui associer la classe suivante.
                signatures[signature] = prochaine_classe
                prochaine_classe += 1
            nouvelle_classe[etat] = signatures[signature] # Donc pour la signature dans signature qu'on a ajoutée,
            # On associe à l'état de la nouvelle classe en traitement la signature qui possède les valeurs de la classes.

        if nouvelle_classe == classe : # Condition expliquée plus haut.
            break

        classe = nouvelle_classe
        # Si ce n'est pas le cas, on fait en sorte que la classe actuelle soit celle en traitement.

    return classe

def constructeur_classes(classe) :
    classes = {} # On crée un dictionnaire qui va contenir les classes.
    for etat, niveau in classe.items() : # On parcourt la classe.
        if niveau not in classes : # Si elle n'est pas dans le dictionnaire, on crée l'entrée.'
            classes[niveau] = [] # Sinon, on l'ajoute.
        classes[niveau].append(etat) # On ajoute l'état dans la classe correspondante.
    return classes

def constructeur_automate(Automate, classes,) :
    alphabet = sorted(Automate["alphabet"]) # On retrie l'alphabet pour éviter de mettre tout en paramètres...
    transitive = table_de_transition(Automate) # Donc, on recrée également la table de transition.
    etats = [] # On initialise la liste d'états.

    lien = {} # On crée un dico lien, il servira à lier les nouveaux états et leur ancien état.
    for classe, etat in classes.items() : # Parcourant les éléments de classes.
        nouvel_etat = int("".join(map(str, sorted(etat)))) # On utilise map pour que chaque
        # Occurrence dans classes devienne un str pour au final les join et repasser en int.
        etats.append(nouvel_etat) # On ajoute le nouvel état qui est un int composé.
        for e in etat : # Et en ce qui concerne le lien, on associe à l'état son nouvel état.
            # EX : 4 = 47, 7 = 47.
            lien[e] = nouvel_etat

    transitions = [] # On initialise la liste des transitions.
    for classe, etat in classes.items() :
        e = etat[0] # On prend le premier état de la classe.
        source = lien[e] # On récupère le nouvel état composé, associé.
        for i, lettre in enumerate(alphabet) : # On garde trace de l'indice.
            ancienne_destination = transitive[e][i] # On regarde la table, on récupère la destination.
            destination = lien[ancienne_destination] # On récupère l'état composé de la destination.
            transitions.append([source, lettre, destination])
            # On ressort avec un format composé, lettre composé. EX : 47, "a", 35

    initiaux = list(set(lien[i] for i in Automate["I"])) # On récupère le composé sans doublons.
    finaux = list(set(lien[f] for f in Automate["F"])) # Des états i et f dans leurs listes respectives.

    return {
        "alphabet": alphabet,
        "etats": etats,
        "transitions": transitions,
        "I": initiaux,
        "F": finaux
    }

if __name__ == "__main__" :
    # print(table_de_transition(automate_minimisation_cours))
    # print(minimisation(automate_minimisation_cours))
    #
    print(minimisation(TueurDeProcesseur))
    print(classes_equivalentes(TueurDeProcesseur))
    print(table_de_transition(TueurDeProcesseur))