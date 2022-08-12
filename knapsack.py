# Uses python3
import sys

def optimal_weight(W, golds):
    d = [[True] + [False] * W]

    for i in range(len(golds)):
        d.append(d[-1][:])

        for w in range(golds[i], W + 1):
            d[-1][w] = d[-2][w] or d[-2][w - golds[i]]
        d = d[-1:]

    for w in range(W, -1, -1):
        if d[-1][w]:
            return w

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
