def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(1)
test(1,"asdasd")
test(1132,123 ,123, 123,13)
test(1132,123 ,123, 123,13, test=123)
test(1132,123 ,123, 123,13, test=123, ok=312)