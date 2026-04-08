"""
Napisz program, który stworzy generator generujący liczby od `0` do podanej wartości (parametru `limit`) z krokiem `1`.
Utwórz dwa obiekty tego generatora z parametrem `limit` równym `5` i wywołuj je asynchronicznie (na zmianę).
"""

def gen(limit):
    for i in range(limit):
        yield i

g1 = gen(5)
g2 = gen(5)

print(f"Generator 1: {next(g1)}")
print(f"Generator 2: {next(g2)}")
print(f"Generator 1: {next(g1)}")
print(f"Generator 1: {next(g1)}")
print(f"Generator 1: {next(g1)}")
print(f"Generator 1: {next(g1)}")
print(f"Generator 2: {next(g2)}")
