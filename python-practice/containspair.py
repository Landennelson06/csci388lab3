def check(l: list):
    found = set()
    for x in l:
        if x in found:
            return True
        found.add(x)
    # your code goes here
    return False


print(check([1, 2, 3, 2]))          # should print True
print(check([5, 2, -10, 44, 90]))   # should print False







