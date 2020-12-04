##integer value

x = 1

print(x)

##deciaml value

x1 = 1.3

print(x1)

##string

x2 = "This is some text"
print(x2)

##boolean
x3 = False
x4 = True

print(x3)
print(x4)

##lists

##intergers
l1 = [1,2,3,4,5,6,7,8,9,10]

print(l1)

##list multiple

l2 = [1, "Hello", 1.7, "Yes", "No"]
print(l2)

##alter value of list
l2[0] = 2
print(l2)

##remove element

##Dictionaries
d1 = {
    "name":"Dog",
    "height":2,
    "races":["bulldog","cockapoo"]
}
print(d1)

print(d1["name"])

l3 = [d1,d1,d1]

print(l3)

##dictionary inside dictionary

d2 = {
    "name": "wolf pack",
    "wolves": [
        {"name": "John", "colour":"grey"}
    ]
}

## practice 1

name = "Kieran"
age = 24
job = "Grad"

work = {
    "name":name,
    "age":age,
    "job":job
}

print(work)

