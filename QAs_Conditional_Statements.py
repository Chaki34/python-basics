
# # Q1 : Write a program to find the greatest of four numbers entered by the user.

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))

# if (num1 >= num2) and (num1 >= num3) and  (num1 >= num4) :
#     print("The greatest number is: ", num1)
# elif (num2 >= num1) and (num2 >= num3) and  (num2 >= num4) :
#     print("The greatest number is: ", num2)
# elif (num3 >= num1) and (num3 >= num2) and  (num3 >= num4) :
#     print("The greatest number is: ", num3)
# else:
#     print("The greatest number is: ", num4) 



# # # Q2 : Write a program to find out whether a student has passed or failed if it requires a
# # total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# # take marks as an input from the user

# math = float(input("Enter marks for Math: "))
# science = float(input("Enter marks for Science: "))
# english = float(input("Enter marks for English: "))

# total_marks = sum([math, science, english])

# avg = total_marks / 3 

# if(avg >= 40) and  (math >= 33) and (science >= 33) and (english >= 33):

#     print(f"total marks is : {total_marks} out of 300 and average is : {avg}")
    
#     print("Congratulations! You have passed.")
# else:
#     print("Sorry, you have failed.")


# # Q3 : A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams. 

# comments = {
#     "comment1": "This is a great product! I highly recommend it.",
#     "comment2": "Make a lot of money by using this amazing product!",
#     "comment3": "I just bought this, and it's fantastic!",
#     "comment4": "Subscribe this channel for more awesome content.",
#     "comment5": "Click this link to get a special discount on your purchase.",
#     "comment6": "I love this! It's the best thing I've ever bought.",
#     "comment7": "Buy now and get 50% off!",
#     "comment8": "This product quality is really good.",
#     "comment9": "Make a lot of money fast with this trick!",
#     "comment10": "Totally worth the price.",
#     "comment11": "Click this link to win a free iPhone!",
#     "comment12": "Very useful and easy to use.",
#     "comment13": "Subscribe this channel and earn online.",
#     "comment14": "I am very satisfied with this purchase.",
#     "comment15": "Buy now before the offer ends!",
#     "comment16": "Amazing experience, will buy again.",
#     "comment17": "click this money from home easily.",
#     "comment18": "Highly recommended for everyone.",
#     "comment19": "Click this link for exclusive deals.",
#     "comment20": "The packaging was very nice.",
#     "comment21": "Subscribe this for daily income tips.",
#     "comment22": "This is not worth the money.",
#     "comment23": "Buy now and become rich!",
#     "comment24": "Great service and fast delivery.",
#     "comment25": "Make a lot of money without effort!",
#     "comment26": "I didn't like the product much.",
#     "comment27": "Click this link and earn instantly.",
#     "comment28": "Subscribe this channel for passive income.",
#     "comment29": "Best purchase I’ve made this year.",
#     "comment30": "buy now! Limited stock available."
# }

# spam_keywords = ('Make a lot of money', 'buy now', 'subscribe this', 'click this')

# for i in comments :

#     if(spam_keywords[0] in comments[i].lower()) or (spam_keywords[1] in comments[i].lower()) or (spam_keywords[2] in comments[i].lower()) or (spam_keywords[3] in comments[i].lower()):

#         print(f"{comments[i]}  <- is a spam comment.\n")


# # Q4 : Write a program to find whether a given username contains less than 10
# characters or not
    

username  = input("enter your username : ")

if len(username) < 10:
    print("Username is too short. Please enter a username with exactly 10 characters.")
elif len(username) > 10:
    print("Username is too long. Please enter a username with exactly 10 characters.")    
else:
    print("Username is valid.")



# Q5 : Write a program to find out whether a given post is talking about “Harry” or not.

posts = {

    "post1": "I just finished reading the latest Harry Potter book, and it was amazing!",
    "post2": "Had a great day at the park with friends.",
    "post3": "Harry is my favorite character in the series.",
    "post4": "Looking forward to the weekend!",
    "post5": "Just watched a movie, it was fantastic."
}

for i in posts :

    if "harry" in  posts[i].lower() :
        print(f"{posts[i]}  <- is talking about Harry.\n")

