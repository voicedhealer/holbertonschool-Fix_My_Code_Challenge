# holbertonschool-Fix_My_Code_Challenge

Basé sur les informations disponibles sur les défis "Fix My Code" de Holberton School et l'exercice FizzBuzz que nous avons analysé, voici un README complet pour le repository :

# holbertonschool-Fix_My_Code_Challenge

## Description

Ce repository contient une série de défis de débogage de code proposés par Holberton School. L'objectif est de développer les compétences de résolution de problèmes en identifiant et corrigeant des bugs dans du code préexistant, couvrant plusieurs langages de programmation [web:22].

Le principe est simple : au lieu de créer du code from scratch, il faut analyser, comprendre et corriger des programmes défaillants. Cette approche reflète fidèlement les défis rencontrés dans l'industrie tech [web:24].

## Structure du Projet
```
holbertonschool-Fix_My_Code_Challenge/
├── README.md              # Documentation du projet
├── challenge/             # Dossier contenant les exercices
│   ├── 0-fizzbuzz.py     # Challenge FizzBuzz (Python)
│   ├── 1-print_square.js # Challenge carré (JavaScript)
│   ├── 2-sort.rb         # Challenge tri (Ruby)
│   ├── 3-user.py         # Challenge classe User (Python)
│   └── 4-delete_dnodeint # Challenge liste doublement chaînée (C)
└── original_buggy_files/  # Fichiers originaux avec bugs
```
## Langages Couverts

- **Python** (~39.1%) - Logique algorithmique, POO
- **C** (~49.3%) - Structures de données, gestion mémoire
- **JavaScript** (~5.9%) - Fonctions, manipulation DOM
- **Ruby** (~5.7%) - Algorithmes de tri [web:22]

## Exercices Détaillés

### 0. FizzBuzz (Python)
**Problème identifié :** Ordre incorrect des conditions
- Les multiples de 15 doivent être vérifiés avant les multiples de 3 et 5
- Solution : Restructurer les conditions if/elif

### 1. Print Square (JavaScript)
**Problème :** Base incorrecte dans parseInt()
- Correction de la fonction d'analyse des entiers [web:23]

### 2. Sort Algorithm (Ruby)  
**Problème :** Algorithme de tri défaillant
- Implémentation correcte du bubble sort [web:23]

### 3. User Class (Python)
**Problème :** Erreurs dans la classe User
- Correction des méthodes et attributs [web:23]

### 4. Delete Node (C)
**Problème :** Fonction delete_dnodeint_at_index défectueuse
- Gestion correcte des pointeurs dans les listes doublement chaînées [web:23]

## Méthodologie d'Apprentissage

Ce projet suit la pédagogie Holberton School basée sur :
- **Learning by doing** : Apprentissage par la pratique [web:24]
- **Peer learning** : Collaboration entre étudiants [web:25] 
- **Problem-solving** : Développement de l'autonomie de recherche [web:28]

## Utilisation

### Prérequis
- Python 3.x
- GCC (pour les fichiers C)
- Node.js (pour JavaScript)
- Ruby (pour les fichiers Ruby)

### Exécution

# Clone du repository
git clone https://github.com/voicedhealer/holbertonschool-Fix_My_Code_Challenge.git
cd holbertonschool-Fix_My_Code_Challenge/challenge

# Test des solutions
python3 0-fizzbuzz.py 50
node 1-print_square.js
ruby 2-sort.rb
python3 3-user.py
gcc 4-delete_dnodeint/*.c -o test && ./test


## Compétences Développées

- **Débogage systematique** : Identification méthodique des erreurs
- **Analyse de code** : Compréhension de code existant [web:28]
- **Multi-langages** : Adaptabilité entre technologies différentes
- **Résolution de problèmes** : Approche logique et structurée [memory:4]

## Standards de Code

- Style respectueux des conventions de chaque langage
- Comments explicatifs sur les corrections apportées
- Tests de validation pour chaque correction
- Documentation des changements effectués

## Ressources d'Apprentissage

- [Holberton School Methodology](https://www.holbertonschool.com) [web:24]
- [Project-based Learning](https://www.holbertoncoderise.com) [web:25]
- Documentation officielle de chaque langage

## Progression et Évaluation

- ✅ Mandatory : Exercices obligatoires
- 📈 Points : Système de notation /5
- 🔄 Resubmission : Possibilité de correction après feedback [web:27]

## Auteur

Étudiant Holberton School - Formation Software Engineering
Apprentissage du débogage et résolution de problèmes [memory:4]

---

*Ce repository fait partie du curriculum Holberton School axé sur l'apprentissage collaboratif et par projet* [web:22][web:24]


Ce README reflète la philosophie d'apprentissage de Holberton School tout en documentant spécifiquement les défis de débogage de code, incluant l'analyse du problème FizzBuzz que nous avons identifié ensemble.
