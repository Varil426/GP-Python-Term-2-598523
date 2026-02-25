import re

"""
Sprawdz czy w tekście występuje cyfra.
"""

sentence = "Uczę się programowania w języku python3"
pattern = r"\d"
result = re.search(pattern, sentence)

if result is None:
    print(f"W zdaniu '{sentence}' nie znaleziono cyfry")
else:
    print(f"W zdaniu '{sentence}' znaleziono cyfrę. Match: {result.group()}")