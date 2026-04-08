"""
Zaimplementuj program, który sortuje listę liczb w oparciu o wartość ich kwadratów (liczba podniesiona do potęgi drugiej).
Na przykład, dla listy `[3, -2, 5, -4]`, jej kwadraty to `[9, 4, 25, 16]`, a wynikowa lista po sortowaniu to `[-2, 3, -4, 5]`.
"""


def sort_by_square(data):
    return sorted(data, key = lambda x: x**2)


print(sort_by_square([1, -2, 0.5, 4, -3]))  # [0.5, 1, -2, -3, 4]
print(sort_by_square([3, -2, 5, -4]))  # [-2, 3, -4, 5]
