t = input("Enter list of tuple: ")
a = tuple(x for x in t.split())
l = list(a)
l.remove(input("Enter an element to remove: "))
a = tuple(l)
print(a)
