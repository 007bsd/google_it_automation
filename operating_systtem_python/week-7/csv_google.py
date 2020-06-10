import csv

f = open("guests.txt")
csv_f = csv.reader(f)

for row_csv in csv_f:
    name, number, role = row_csv
    print("Name: {}, Number: {}, Role: {}".format(name, number, role))
f.close()


hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "108.168.25.46"]]

with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

with open("hosts_row.csv") as hosts_check:
    reader = csv.DictReader(hosts_check)
    for row_hosts in reader:
        print("{} hosts and {} number".format(row_hosts["name"], row_hosts["ip"]))

users = [{"name": "john", "username": "john123", "department": "IT"},
         {"name": "Kari", "username": "Kari123", "department": "HR"},
         {"name": "Tomi", "username": "Tomi123", "department": "FINANCE"}]

keys = ["name", "username", "department"]

with open('by_department.csv', "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row

def contents_of_file(filename):
    return_string = ""
    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open("flowers.csv") as flowers_csv:
        reader_flowers = csv.DictReader(flowers_csv)
    # Read the rows of the file into a dictionary
        for row in reader_flowers:
         # Process each item of the dictionary
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))


import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

  # Call the function to create the file
    create_file(filename)

  # Open the file
    flowers_file = open(filename)
    # Read the rows of the file
    rows = csv.reader(flowers_file)
    next(rows, None)
    # Process each row
    for row in rows:
        name_flower, flower_color, flower_type = row
      # Format the return string for data rows only
        return_string += "a {} {} is {}\n".format(flower_color, name_flower, flower_type)
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))