##simplpe function without input or output
#def func1():
#    print("Hello World!")

#func1()


##simple function with input and output
#def sausage_maker(pig):
#    return "sausages of "+pig

#sausage = sausage_maker("Kieran")
#print(sausage)

#print(sausage_maker("Peggy"))

##simple function with input no output
#def add(x,y):
#    return x+y

##create a func that receives(input) of list
##outputs a loist of the values multiplied by two

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [2,4,6,8,10]

def multiply_by_2_list(l):
    aux = []

    for value in l:
        aux.append(value * 2)

    return aux

out1 = multiply_by_2_list(l1)

print(out1)

out2 = multiply_by_2_list(l2)

print(out2)

##create a func that receives(input) of list
##outputs a loist of the values divide by two

def divide_by_2_list(l):
    aux = []

    for value in l:
        aux.append(value / 2)

    return aux

out1 = divide_by_2_list(l1)
out2 = divide_by_2_list(l2)

print(out1)
print(out2)

kieran = {
    "name":"Kieran",
    "age":24,
    "gender":"male"
}

def is_male(person):

    gender = person["gender"]
    if gender == "male":
        return True
    else:
        return False

is_kieran_male = is_male(kieran)

print("Is Kieran a male?", is_kieran_male)

def is_female(person):

    gender = person["gender"]
    if gender == "female":
        return True
    else:
        return False

is_kieran_female = is_female(kieran)

print("Is Kieran a female?", is_kieran_female)

##create a function that checks if a person is older than 30 years old

def older_than_thirty(person):

    age = person["age"]
    if age >= 30:
        return True
    else:
        return False

is_kieran_older_than_30 = older_than_thirty(kieran)

print("Is Kieran older than 30?", is_kieran_older_than_30)

##create a function that receves a list then outputs the numbers divisible by 2

l1 = [1,2,3,4,5,6,7,8,9,10]

def numbers_divisible_by_2(l):

    aux = []

    for value in l:
        if value % 2 == 0:
            aux.append(value)

    return aux

nums_divisible_by_two = numbers_divisible_by_2(l1)

print(nums_divisible_by_two)

##create a function that retrieves male people over 30 years old

sophia = {
    "name":"Sophia",
    "age":25,
    "gender":"female"
}

people = [
    kieran,
    sophia,
    {
        "name":"Lucas",
        "age":40,
        "gender":"male"
    }
]

def get_males_over_30(list_of_people):
    aux = []

    for person in list_of_people:
        if older_than_thirty(person) and is_male(person):
            aux.append(person)

    return aux

get_males = get_males_over_30(people)

print(get_males)