import pytest
def facto(n):
    #this is a misunderstanding of factorisation I guess
    if n < 0:
        return None
    if n < 2:
        return 1
    return n + facto(n-1)
def facto2(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n*facto2(n-1)

for n in range(1, 10):
    print(n, "->", facto2(n))
