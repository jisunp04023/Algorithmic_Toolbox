#Uses python3

import sys

def max_dot_product(a, b):
    n = len(a)
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
