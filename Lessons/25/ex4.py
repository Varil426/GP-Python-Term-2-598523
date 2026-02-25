import re

"""
Znajdź wszystkie daty w formacie DD-MM-YYYY z tekstu.
"""

sentence = "Dzisiaj jest 20-10-2024, a jutro będzie 21-10-2024."

result = re.findall(r"\d{2}-\d{2}-\d{4}", sentence)
print(result)