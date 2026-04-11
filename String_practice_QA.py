
# # Q1:Write a python program to display a user entered name followed by Good
# Afternoon nwith today date using input () function

import datetime

name  = input("Enter your name :")
print("Good Afternoon " + name)
print("Today's date is : " + str(datetime.date.today()))

# get only time  
# this datetime.datetime.now() return total data & time but we want only time so we use .time() method to get only time
print("Current time is : " + str(datetime.datetime.now().time()))


# Q1: Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
 Dear <|Name|>,
 You are selected!
 <|Date|>
'''

name = input("Enter your name: ")

date = datetime.datetime.now().strftime("%Y-%m-%d")

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)

#Q1 : Write a program to detect double space in a string

text = input("Enter a string: ")

space_count = text.count(" ")

if space_count == 1:
    print("single space found!")

elif space_count > 1:
    print("multiple spaces found!")

else:
    print("no space found!")


#Q3 :Write a program to format the following letter using escape sequence characters.

letter = "Dear Harry, this python course is nice. Thanks!"


letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"

print(letter)






