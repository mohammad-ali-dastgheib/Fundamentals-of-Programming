def harmonic(n):
    s = 0
    for i in range(n):
        term = 1 / (i+1)
        s+= term
    return s

n = int(input("what is n? "))
print(harmonic(n))
