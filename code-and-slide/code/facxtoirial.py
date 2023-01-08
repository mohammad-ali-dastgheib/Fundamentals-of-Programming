def factoriel(n):
    if n == 0:
        return 1
    k=n*factoriel(n-1)
    return k

k=int(input())
print(factoriel(k))
