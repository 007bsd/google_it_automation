guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")


dir = "text"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as f:
    filesize = f.write(comments)
  return(filesize)

print(create_python_script("program.py"))

import os

import os
def new_directory(directory, filename):
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    os.chdir(directory)
    with open(filename, 'w') as f:
            pass
    return(os.listdir())
print(new_directory("PythonPrograms", "script.py"))

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w') as f:
      pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  new_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(new_timestamp))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())
