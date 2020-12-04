##practice 3

numbers_1_to_10 = [1,2,3,4,5,6,7,8,9,10]
numbers_1_to_10_multiplied2 = []

for n, item in enumerate(numbers_1_to_10):
    print(n, "->", numbers_1_to_10[n] *2)

    numbers_1_to_10_multiplied2.append(numbers_1_to_10[n]*2)
print(numbers_1_to_10_multiplied2)



names1 = ["Marco", "George", "Kieran", "Robin"]
names2 = []

for value in names1:
    #print(value)

    names2.append(value)
print(names2)



ages2 = [10,20,40,30,10,57]
ages3 = []

for value in ages2:
    print(value)
    if value < 30:
        ages3.append(value)

print(ages3)

people = [
    {
        "name":"Marco",
        "age": 30
    },
    {
        "name":"Kieran",
        "age": 20
    },
    {
        "name":"Robin",
        "age": 10
    },
{
        "name":"George",
        "age": 40
    }
]

people_over_30 = []
people_below_30 = []

for value in people:
    #print(value)
    if value["age"] <= 30:
        people_below_30.append(value)
    if value["age"] >= 30:
        people_over_30.append(value)

print(people_below_30)
print(people_over_30)