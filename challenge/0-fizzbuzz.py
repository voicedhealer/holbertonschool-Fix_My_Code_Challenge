#!/usr/bin/python3

def fizzbuzz(n):
    """
    Fonction qui affiche les nombres de 1 à n avec:
    - 'Fizz' pour les multiples de 3
    - 'Buzz' pour les multiples de 5
    - 'FizzBuzz' pour les multiples de 3 ET 5
    - Le nombre pour les autres cas
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# Gestion des arguments de ligne de commande
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: ./0-fizzbuzz.py <number>')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        fizzbuzz(n)
    except ValueError:
        print('Erreur: Veuillez entrer un nombre entier')
        sys.exit(1)
