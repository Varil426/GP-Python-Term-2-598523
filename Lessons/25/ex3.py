import re

"""
Zamień wszystkie lata z tekstu na rok 2137.
"""

sentence = "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1]) – polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), epizodycznie związany z mesjanizmem polskim, był też mistykiem. Obok Adama Mickiewicza uznawany powszechnie za największego przedstawiciela polskiego romantyzmu."

pattern = r"\d{4}"
repl = "2137"

result = re.sub(pattern, repl, sentence)

print(result)