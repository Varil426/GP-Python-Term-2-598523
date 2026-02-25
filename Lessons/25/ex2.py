import re

"""
Znajdź wszystkie daty w zdaniu.
"""

sentence = "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1]) – polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), epizodycznie związany z mesjanizmem polskim, był też mistykiem. Obok Adama Mickiewicza uznawany powszechnie za największego przedstawiciela polskiego romantyzmu."

pattern = r"\d{1,2}\s\w+\s\d{1,4}"
result = re.findall(pattern, sentence)

print(result)