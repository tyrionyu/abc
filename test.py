def func():
    output = 0
    while True:
        new = yield output
        output = new

genr = func()

print(next(genr))
print(next(genr))
print(next(genr))