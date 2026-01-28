"""
Z podanego ciągu znaków usuń znaki nie będące literami ani cyframi.
"""

string = "hello@123world!456"

# wynik = [znak for znak in string if znak.isalpha() or znak.isdigit()]
wynik = [znak for znak in string if znak.isalnum()]
print("".join(wynik))
