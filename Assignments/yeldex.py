def get(n):
    for i in range(n):
        print(i)
    yield

print(next(get(5)))

