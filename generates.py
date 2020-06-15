def create(n):
    for x in range(n):
        yield (x**3)
for x in create(10):
    print(x)