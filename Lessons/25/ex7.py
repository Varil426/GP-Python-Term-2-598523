import re

"""
Znajdź wszystkie słowa zaczynające się na literę `s` i kończące na literę `t`.
"""

sentence = "start script level loop debug player server tournament map speedrun quest socket"

result = re.findall(r"\bs\w*t\b", sentence)
print(result)