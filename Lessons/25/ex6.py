import re

"""
Znajdź wszystkie wyrazy zawierające przynajmniej 2 samogłoski.
"""

sentence = "start script level loop debug player server tournament map speedrun quest socket"

pattern = r"\b\w*(?:[aeiouy]\w*){2,}\b"

result = re.findall(pattern, sentence, re.I)

print(result)