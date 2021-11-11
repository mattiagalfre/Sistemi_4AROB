x = [0, 1, 2, 3, 5, 6, 7, 8]
y = x[:len(x)//2]       #divisione di interi -> a//b     divisione float -> a/b     elevamento a potenza -> a**b       modulo -> a%b
z = x[len(x)//2:]
print(x)
print(y)
print(z)

y.append(5)
print(y)
