
file = open("D:\\Python Basics Code\\File_Hadeling\\filetest.txt", "w") # open a file and also create if not exist

file.write("Hello, this is a test file.\n") # write to the file
file.write("This file is used for demonstrating file handling in Python.\n")    

# to write multiple lines we can use writelines() method which takes a list of strings as input and writes them to the file
lines = ["hello my name is debmalya \n", "i am a programmer \n", "i love to design softwares \n"]
file.writelines(lines)

file.close() # always remember to close the file after you're done with it

# good practice : 

with open("D:\\Python Basics Code\\File_Hadeling\\myfile.txt", "w") as file:
    file.write('''This is a good practice to use 'with' statement for file handling because it 
                           automatically takes care of closing the
                        file after the block of code is executed, even if an error occurs.\n''')   
    
    # not need to explicitly call file.close() when using 'with' statement, it will be done automatically.


    file.write("This is another line in the file.\n")
    file.write("This file is used for demonstrating good practices in file handling in Python.\n")

    list = ["This is line 1\n", "This is line 2\n", "This is line 3\n"]
    file.writelines(list)

#   modify the file by opening it in append mode

with open("D:\\Python Basics Code\\File_Hadeling\\filetest.txt", "a") as file:
    file.write("This line is added in append mode.\n")
    file.write("This line is also added in append mode.\n")

# read a file 

with open("D:\\Python Basics Code\\File_Hadeling\\filetest.txt", "r") as file:
    content = file.read() # read the entire content of the file
    print(content) 


    # if we need to read line by line  

print("---------------------------------------------------------------")
with open("D:\\Python Basics Code\\File_Hadeling\\filetest.txt", "r") as file:
    for lines in file :
        print(lines) # this will print each line of the file one by one

# Q1 : find emails from a exisiting myfile file and write those emails to a new file called "emails.txt"


# if need to show as a row string so use  r "file path" it is workable for read , but for write we need to use double backslash \\ or single forward slash / in the file path to avoid escape character issues.

with open("D:\\Python Basics Code\\File_Hadeling\\data.txt", 'r') as file:
    content = file.read()

    words = content.split()

    with open("D:\\Python Basics Code\\File_Hadeling\\emails.txt", "w") as email_file:

        for word in words:
              # ✅ remove punctuation
            if '@' in word:
                print(word)  # ✅ print the email to console
                email_file.write(word + '\n')




# # Q2 : Write a program where user put all necesory details and tthis details used to make a profile like resume  and write the file name with the username  


# name = input("Enter your name: ")
# age = input("Enter your age: ")
# email = input("Enter your email: ")
# phone = input("Enter your phone number: ")
# degree = input("Enter your degree: ")
# experience = input("Enter your experience: ")
# address = input("Enter your address: ")
# skills = input("Enter your skills: ")
# github = input("Enter your github profile link: ")


# profile_content = f"""
# ================= 👨‍💻 DEVELOPER PROFILE =================

# 🧑 Name        : {name}
# 🎂 Age         : {age}
# 📧 Email       : {email}
# 📱 Phone       : {phone}

# ---------------------------------------------------------

# 📝 PROFILE SUMMARY
# I am {name}, a motivated software developer with {experience} of experience.
# My academic background in {degree} has helped me build a strong foundation in 
# programming and problem-solving. I specialize in {skills} and love working on 
# innovative projects that make an impact. I am always eager to learn new technologies 
# and contribute to meaningful development work.

# ---------------------------------------------------------

# 🎓 EDUCATION
# {degree}

# 💼 EXPERIENCE
# {experience}

# ---------------------------------------------------------

# 🛠️ TECHNICAL SKILLS
# {skills}

# ---------------------------------------------------------

# 🌐 GITHUB / PORTFOLIO
# {github}

# ---------------------------------------------------------

# 📍 ADDRESS
# {address}

# =========================================================
# """

# with open(f"D:\\Python Basics Code\\File_Hadeling\\{name}_profile.txt", "w", encoding="utf-8") as profile_file:
#     profile_file.write(profile_content)


 
# if we read a file in binary : 

with open("File_Hadeling\emails.txt", "rb") as file:
    data = file.read()
    print(data)
    print(type(data))

# if read in chunks  


with open("File_Hadeling\emails.txt", "rb") as file:
    chunk = file.read(10)   # read 10 bytes
    print(chunk)


# String to binary and store into a file  

# 🔹 Step 1: Read normal text from file
with open(r"File_Hadeling\emails.txt", "r", encoding="utf-8") as file:
    text_data = file.read()   # this is normal string (emails, text, etc.)


# 🔹 Step 2: Convert text → binary
# Each character → ASCII → binary (8-bit)
binary_data = ' '.join(format(ord(char), '08b') for char in text_data)


# 🔹 Step 3: Write binary data into a new file
with open(r"File_Hadeling\binary_output.txt", "w") as file:
    file.write(binary_data)


print("✅ Text successfully converted to binary and saved!")


# read the data  
print(" Data : \n\n")
with open("File_Hadeling/binary_output.txt", "rb",) as file:
    data = file.read()
    print(data) 


# read a image file  - 

print("Image  Data : \n\n")
with open("File_Hadeling/water-melon.png", "rb") as file:
    data = file.read()

    print(data)

print(type(data))  # <class 'bytes'>






    

