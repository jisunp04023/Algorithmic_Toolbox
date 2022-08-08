# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    first = 0
    second = 1
    res = 0
    
    for i in range(2, n+1):
        res = (first + second) % 10
        first = second
        second = res
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
