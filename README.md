# SAÉ 2.02 : Graphes & Automates

Projet de BUT Informatique (SAÉ 2.02) : manipulation d'automates finis en Python, de la lecture d'un mot jusqu'à la minimisation.

## Équipe

- Miodrag ANTONIJEVIC
- Valentin FOURREAU--HARELLE

## Contenu

Le projet est découpé en six parties, chacune dans son dossier :

| Partie | Contenu |
|---|---|
| `Partie1` | Mots (préfixes, suffixes, facteurs, miroir), langages (concaténation, puissance, tous les mots d'une longueur donnée) et automates (définition, lecture d'un mot, acceptation) |
| `Partie2` | Déterminisme et déterminisation d'un automate, renommage des états |
| `Partie3` | Complétion et complémentaire d'un automate |
| `Partie4` | Automate produit : intersection et différence |
| `Partie5` | Émondage et propriétés de fermeture (préfixe, suffixe, facteur, miroir) |
| `Partie6` | Minimisation : table de transition, classes d'équivalence, construction de l'automate minimal |

## Utilisation

Le projet nécessite Python 3. Les modules s'importent depuis la racine du dépôt, par exemple :

```python
from Partie1.Langages import tousmots
```

Lancez donc vos scripts depuis la racine du dépôt.
