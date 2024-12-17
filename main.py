# 1 Name Shuffler
def almashtirish(name):
    a = name.split()
    return ' '.join(a[::-1])

john = "john McClane"
result = almashtirish(john)
print(result)