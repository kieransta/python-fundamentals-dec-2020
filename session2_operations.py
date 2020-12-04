## add operation

print("1+1 =",1+1)

x1 = 1
x2 = 2

print("x1 + x2 =", x1+x2)

##minus

print("x1-x2 =", x1-x2)

##multiply

print("x1 * x2 =", x1*x2)

##divide

print("x1/x2 =", x1/x2)

##mod

print("x1 % x2 =", x1%x2)

##add and then multiply

print("(x1 + x2) *2 =",(x1 +x2) * 2)

x3 = x1 + x2

print("x3 =",x3)

##Stirng Operations

s1 = "Hello"
s2 = "World"

s3 = s1 + " " + s2 + "!"

print(s3)

#the following will return an error as strings are not supported
#s4 = s1 - s2
#print(s4)

##Mixed Values
#convert x1 to a string for operation to be valid
s4 = s1 + str(x1)

#convert string to number
#s5 = int(s1)
s6 = "6"
x5 = int(s6)

print(s4)
print(s6)

##boolean

have_hair = True
have_moustache = False

have_hair_and_moustache = have_hair and have_moustache

print(have_hair_and_moustache)