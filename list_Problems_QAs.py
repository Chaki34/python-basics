# Q1: Store 7 fruits and print in uppercase

import numbers


def function():
    # empty list to store fruits
    fruits = []

    # take 7 fruit names from user
    for i in range(7):
        fruit = input("Enter the name of a fruit: ")  # FIXED
        fruits.append(fruit)

    # print header
    print("Fruits in uppercase:")

    # print fruits in uppercase
    for fruit in fruits:
        print(fruit.upper())


# Q2: Accept marks of 6 students and display sorted

def function1():
    marks = []

    for i in range(6):
        mark = int(input("Enter marks: "))
        marks.append(mark)

    marks.sort()

    print("Marks in sorted manner:")
    for mark in marks:
        print(mark)




# Q3 : Write a program to sum a list with 4 numbers.

def function2():
    numbers = []

    for i in range(5):
       num = input("Enter your number :");
       numbers.append(num) # we are appending string to list 

    total = map(float,numbers) # Convert strings to floats using map function  

    total = sum(total)  # Convert strings to integers and sum them

    print("The sum of the numbers is:", total)     



def function3():
    # Q5 : Write a program to count the number of zeros in the following tuple:
    a = [7, 0, 8, 0, 0, 9]

    zero_count = a.count(0)  # Count the number of zeros in the list
    print("Number of zeros in the list:", zero_count)




#function1()

function3()

