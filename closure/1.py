def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3
