def memoize(func):
    cache = {}
    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return inner

def expensive_function(x):
    print(f"Calculating... for {x}")
    return x ** 2

memoized_expensive_function = memoize(expensive_function)

print(memoized_expensive_function(3))
print(memoized_expensive_function(3))
print(memoized_expensive_function(4))
print(memoized_expensive_function(4))
