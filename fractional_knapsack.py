# Uses python3
import sys

def get_optimal_value(W, value_list, weight_list):
    n = len(value_list)
    lst = []
    
    for i in range(n):
        lst.append((value_list[i], weight_list[i]))

    if W == 0:
        return 0

    lst.sort(key = lambda x: x[0]/x[1], reverse = True)

    total_value = 0

    for v,w in lst:
        if W==0:
            return total_value
        amt = min(w, W)
        total_value += amt*v/w
        W -= amt

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, values, weights)
    print("{:.10f}".format(opt_value))
