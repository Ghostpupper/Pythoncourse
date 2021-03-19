def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(2, 12):
    print(n-1, "    ->", fib(n))