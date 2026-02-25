import re

"""
Znajdź liczby nieparzyste spośród podanych.
"""

sentence = "Podane liczby to 5 12 442 321 45 20 77"

pattern = r"\b\d*[13579]\b"

result = re.findall(pattern, sentence)
print(result)