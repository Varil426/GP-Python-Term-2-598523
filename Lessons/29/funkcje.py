def add(a, b):
    return a + b

def is_palindrom(wyraz):
    return wyraz == wyraz[::-1]

def is_valid_triangle(a,b,c):
    return max(a,b,c) < a+b+c - max(a,b,c) if min(a,b,c) > 0 else False

def divide(a,b):
    try:
        print(a/b)
    except:
        print("Nie dziel przez 0")