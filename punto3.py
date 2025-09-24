import math

def es_primo(N: int, N2: int):
    for i in range(N,N2):
        for j in range(2, int(math.sqrt(i)) + 1):
            if N % j == 0:
                cont
            else:
                cont =+1
    return cont


N = int(input())
N2 = int(input())
print(es_primo(N ,N2))
