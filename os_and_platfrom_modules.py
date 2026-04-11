import os
import psutil
import platform

# Get the current working directory

current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List all files and directories in the current directory

items = os.listdir(current_directory)
print("Items in Current Directory:", items)

print("----------------------------------------")

# find available drives in windows


drives = ["C:/", "D:/", "E:/", "F:/"]

for d in drives:
    if os.path.exists(d):
        print("Available drive:", d)


print("----------------------------------------")


# get all files from the sepcific directory 

directory = "D:/"

files = os.listdir(directory)
print("Files in Directory:", files)

print("----------------------------------------")


# get filders from specific path 

path = "D:/Python Basics Code"

for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isdir(full_path):
        print(item)


print("----------------------------------------")
# window details - 

print("OS Name:", os.name)

# if get full os info - then use platform module



print("===== SYSTEM INFO =====")
print("System        :", platform.system())
print("Node Name     :", platform.node())
print("Release       :", platform.release())
print("Version       :", platform.version())
print("Architecture  :", platform.machine())
print("Processor     :", platform.processor())
print("Platform      :", platform.platform())


# to show all env variables

print("\n===== ENVIRONMENT VARIABLES =====")

print(os.environ)

# if need to get helth cheack , cpu-use then  use psutil module


print("CPU Usage:", psutil.cpu_percent(), "%")
print("RAM:", psutil.virtual_memory().percent, "%")