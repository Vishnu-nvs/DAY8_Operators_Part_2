
a=10
b=20
print("Memory location of A is :",id(a))

print("Memory location of B is :",id(b))

print(a is not b,"\n") # bot variable are pointingg different address.

c=10
d=10

print("Memory location of c is :",id(c))

print("Memory location of d is :",id(d))

print(c is not d)