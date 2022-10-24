# def my_function(name):
#    print("Python", name)


# my_function("Simplilearn")


# def my_function1(name1, name2):
#    print("Python", name1, name2)


# my_function1("Nikiforov", "Martin")


# def my_county(country='Bulgaria'):
#    print("I am from " + country)


# my_county("USA")
# my_county("Russia")
# my_county()


# def my_age(name, age):
#    print(name, "is", age, "years old")


# my_age(age='20', name='John')

# def sum_of(a, b):
#    return a + b


# x = sum_of(4, 7)
# print(x)

# def count(num):
#   if num <= 0:
#       print("Stop")
#   else:
#       print(num)
#       count(num - 1)


# count(5)

# def square(y):
#    return y * y


# for x in range(1, 11):
#   print(square(x))


# def multiply(numbers):
#    total = 1
#    for x in numbers:
#        total *= x
#    return total


# print(multiply((3, 2, 4, 1, 5)))

# def even_odd(num):
#    if num % 2 == 0:
#        return "Even"
#    else:
#        return 'Odd'


# number = int(input())
# print(even_odd(number))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# result2 = list(filter(lambda x: x % 2 != 0, numbers))
# print(result)
# print(result2)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]


# def check_numbers(num):
# if num % 2 == 0:
#  return True
# else:
# return False


# result = list(filter(check_numbers, numbers))
# print(result)

# numbers = list(map(int, input().split(', ')))   # vzima input i go prevrashta v int chisla v spisak

# numbers = [2, 4, 6, 8, 10]


# def imeto_na_funkciqta(number):
#    return number * number


# square_numbers = list(map(imeto_na_funkciqta, numbers))
# print(square_numbers)

# numbers = list(map(int, input().split()))


# ---------------------------------------------------#---------------------------------------------------

# def sum_function(a, b):
#    return a + b


# def subtract_function(a, b):
#    return a - b


# def imeto_na_funkciqta(a, b):
#    print(f"Sum function result: {sum_function(a, b)}")
#    print(f"Subtract function result: {subtract_function(a, b)}")


# imeto_na_funkciqta(5, 1)

# ---------------------------------------------------#---------------------------------------------------

# ITSELF function !!!!!! Rekursiq

#def countdown(number):
#    print(number)

#    if number == 0:
#        return
#    else:
#        countdown(number - 1)


#countdown(5)
