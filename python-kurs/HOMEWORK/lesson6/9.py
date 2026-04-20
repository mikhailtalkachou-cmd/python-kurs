def silna(n: int) -> int:
    if n == 0:
        return 1
    return n * silna(n - 1)

print(silna(4))