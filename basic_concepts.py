a = [3, 4]
factors = [1, 2, 3, 4, 6, 8, 12, 24]
for number in a:
    for factor in factors:  #
        print("number: " + str(number) + " factor: " + str(factor))
        print(factor % number)
        if factor < number or factor % number != 0:
            # remove the factor
            factors.remove(factor)




# tuples - store a sequence of objects that are immutable
numbers = (1, 2, 3)

# Range function - generate a sequence of numbers
numbers = range(5, 10, 2)  # returns a range object that can store a sequence of values
for number in range(5, 10, 2):
    print(number)

# For Loops - iterate over a list and access each item individually
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item * ":D ")

# List Methods
numbers = [1, 2, 3, 4, 5]
numbers.append(7)
numbers.insert(-1, 6)
print(numbers)
print(1 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)

# Lists
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names[-5])
print(names[0:3])
print(names)

# While loops - to repeat a block of code multiple times
i = 1
while i <= 1_000:
    print(i * '*')
    i = i + 1

# Weight converter program
weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight) / 0.45
if unit.upper() == "L":
    converted = float(weight) * 0.45
print("Weight is: " + str(converted))

# if Statements
temperature = 26
if temperature > 25:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's cold")

# Logical Operators
price = 25
print(price > 20 and price < 40)
print(not True)

# Comparison operators
x = 3 > 2
print(x)
x = 3 == 3
print(x)

# Arithmetic Operations
print(10/3)
print(10//3)
print(10 ** 3)
x = 10
x += 3
print(x)  # augmented assignment operator

# Strings
course = "Python for Beginners"
print(course.upper())  # does not change original string, returns new string
print(course.find("for"))
print(course.replace("for","4"))  # strings are immutable therefore creates a new string in memory
print("Python" in course)

# Calculator
first = input("Key in your first number ")
second = input("Key in your second number ")
sum_calc = float(first)+float(second)
print("Sum: " + str(sum_calc))

# Storing variables from  input
name = input("What is your name? ")
print("Hello " + name)
birth_year = input("Enter your birth year ")
age = 2023 - int(birth_year)
print(age)

# Checking in a new patient to a hospital
patient_name = "John Smith"
patient_age = 20
is_new = True
print(patient_age)