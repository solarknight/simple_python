def hello(name):
    return "Hello, " + name

print(hello("Tom"))
print(hello("Lily"))

def contains(s1, s2):
    return s1 in s2

print(contains("Hel", "Hello"))
print(contains("Hel", "hello"))