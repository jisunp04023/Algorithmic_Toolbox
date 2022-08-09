# Uses python3
import sys

def get_change(m):
    denomination_list = [10, 5, 1]
    
    change = []
    
    for coin in denomination_list:
        while m:
            if coin <= m:
                change.append(coin)
                m -= coin
            else:
                break
                
    return len(change)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
