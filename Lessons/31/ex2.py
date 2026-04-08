"""
Napisz program który znajdzie pierwszy unikalny znak w podanej sekwencji znaków.
Na przykład, "ala ma kota, kot jest ali" -> "m", ponieważ "m" jest pierwszym znakiem, który nie powtarza się w ciągu.
"""


def find_unique(string):
    # V1
    # all_characters = []
    # for c in string:
    #     if c not in all_characters:
    #         all_characters.append(c)
    
    # helper = []
    # for c in string:
    #     if c not in helper:
    #         helper.append(c)
    #     elif c in helper and c in all_characters:
    #         all_characters.remove(c)
    # return all_characters[0]

    # V2
    letters = [letter for letter in string if string.count(letter) == 1]
    return letters[0]
    


print(find_unique("ala ma kota, kot jest ali"))
