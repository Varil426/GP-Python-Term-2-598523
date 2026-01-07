from pprint import pprint

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict3 = {**dict1, **dict2}
dict4 = dict1 | dict2

pprint(dict3)
pprint(dict4)