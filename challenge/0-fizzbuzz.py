#!/usr/bin/python3

def fizzbuzz(n):
    """
    Prints numbers from 1 to n with:
    - 'Fizz' for multiples of 3
    - 'Buzz' for multiples of 5
    - 'FizzBuzz' for multiples of both 3 and 5
    Output format: all on one line, space-separated, NO trailing space
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    print(' '.join(result))

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
