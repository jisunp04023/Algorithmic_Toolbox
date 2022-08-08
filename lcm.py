# Uses python3
import sys

def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm_naive(a, b):
    lcm = (a*b) // compute_gcd(a,b)
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

