test = { # Il n'est pas déterministe car a > 1 occurence de lui-même.
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

test2 = { # Il n'est pas déterministe car I > 1.
    "alphabet": ["a", "b", "c", "d"],
    "etats": [1, 2, 3, 4],
    "transitions": [
        [1, "a", 2],
        [2, "b", 3],
        [4, "c", 3],
        [3, "d", 4]
    ],
    "I": [1, 4],
    "F": [3, 4]
}

test3 = { # Il est déterministe car I == 1 && chaque état admet une unique transition pour une même lettre.
    "alphabet": ["a", "b", "c", "d"],
    "etats": [1, 2, 3, 4],
    "transitions": [
        [1, "a", 2],
        [2, "b", 3],
        [4, "c", 3],
        [3, "d", 4]
    ],
    "I": [1],
    "F": [3, 4]
}

# C'est bien gentil de demander nos tests, mais vérifier avec le test du pdf est plus judicieux.

auto2={"alphabet":['a','b'],"etats": [0,1],
       "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

soutenance1={
    "alphabet":['a','b'],
    "etats": [1,2,3],
    "transitions":[
        [1,"b",2],
        [2,"a",2],
        [2,"b",2],
        [2,"a",3],
        [1,"b",3],
        [3,"a",1],
        [3,"a",3]
    ],
    "I":[1,2],
    "F":[3]
}