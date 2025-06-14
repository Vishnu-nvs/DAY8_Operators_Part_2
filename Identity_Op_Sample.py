a=10
print("Memory location of A is :",id(a))
b=10
print("Memory location of B is :",id(b))

print(a is b,"\n") # both are pointing to same address

c=20
d=20.0
print("Memory location of C is :",id(c))
print("Memory location of D is :",id(d))
print(c is d)
