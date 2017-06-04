def print_char(str):
    for c in str:
        print(c)

print_char("Hello")

def nsum(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

print(nsum(10))
