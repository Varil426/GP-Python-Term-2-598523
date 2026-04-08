"""
Napisz program, który z ciągu w formacie: napis, liczba wygeneruje ciąg znaków.
W wygenerowanym ciągu każdy napis powinien zostać powtórzony tyle razy ile wskazuje liczba go poprzedzająca.
Na przykład: kot3ala3c11 -> kotkotkotalaalaalaccccccccccc.
Załóż, że dane zawsze zostaną dostarczone w prawidłowym formacie.
"""

import re


def create_string(text):
    strings = re.findall(r'\D+', text)
    numbers = re.findall(r'\d+', text)
    helper_array = zip(strings, numbers)
    return "".join([word * int(count) for word, count in helper_array])


result = create_string("kot3ala3c11")
print(result)