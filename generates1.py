def Class(n):
    for x in range(n):
        yield x
for number in Class(3):
    print(number)

