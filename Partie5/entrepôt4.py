test_complet = {"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

test_incomplet = {"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'a',1],[1,'b',1]], "I":[0],"F":[1]}


auto2={"alphabet":['a','b'],"etats": [0,1],
       "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

test_incomplet_vaste = { # C'est parti pour bien torturer le CPU...
       "alphabet": ['a', 'b', 'c', 'd', 'e'],
       "etats": [0, 1, 2, 3, 4],
       "transitions": [
              [0, 'a', 1], [0, 'a', 2], # C'est ici qu"il est non déterministe.
              [1, 'b', 3],
              [2, 'c', 4],
              [3, 'd', 0],
              [4, 'e', 1],
              [0, 'c', 3],
              [2, 'a', 2],
              [3, 'b', 4],
              [4, 'a', 0]
       ],
       "I": [0],
       "F": [4]
}

auto4 ={"alphabet":['a','b'],"etats": [0,1,2,],
        "transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}
auto5 ={"alphabet":['a','b'],"etats": [0,1,2],
        "transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],
        "I":[0],"F":[0,1]}

automate_pas_emonde = {
       'alphabet': ['a', 'b'],
       'etats': [0, 1, 2, 3, 4],
       'transitions': [
              [0, 'a', 1],
              [1, 'b', 0],
              [1, 'a', 2],
              [2, 'a', 2],
              [2, 'b', 2],
              [4, 'a', 1]
       ],
       'I': [0],
       'F': [1]
}

automate1 = {
       'alphabet': ['a', 'b', 'c'],
       'etats': [0, 1, 2, 3],
       'transitions': [
              [0, 'a', 1],
              [1, 'b', 2],
              [2, 'c', 3]
       ],
       'I': [0],
       'F': [3]
}