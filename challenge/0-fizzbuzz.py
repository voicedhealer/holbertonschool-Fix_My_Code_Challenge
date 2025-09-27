#!/usr/bin/python3

def fizzbuzz(n):
    """
    Prints numbers from 1 to n with:
    - 'Fizz' for multiples of 3
    - 'Buzz' for multiples of 5  
    - 'FizzBuzz' for multiples of both 3 and 5
    All outputs on the same line separated by spaces
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
    print()  # Final newline

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: ./0-fizzbuzz.py <number>')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        fizzbuzz(n)
    except ValueError:
        print('Error: Please enter a valid integer')
        sys.exit(1)
