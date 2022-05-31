import re
import os

# Global data_list list to store the data from data.txt
data_list = []

# Load data into data_list list
def load_data_into_list():
    with open("data.txt") as file:
        if os.stat("data.txt").st_size != 0:
            for item in file.readlines():
                data_list.append(item)
        else:
            return print("File \"data.txt\" is empty!")
        
        file.close()
    
    return data_list

# Recount/reorder the list from 1, 2, 3, etc...
def count():
    if not data_list:
        return print("There is no data.")
    else:
        for item in range(len(data_list)):
            item += 1
            m = re.match("(\d+\.\s+)(.*)", data_list[int(item) - 1])
            s = data_list[int(item) - 1].replace(m.groups()[0], str(item) + ". ")
            data_list[int(item) - 1] = s
            insert_data_into_file()
        
# Take what's inside data_list and dump it into the data.txt file
def insert_data_into_file():
    with open("data.txt", "w") as file:
        for item in data_list:
            file.write(item)
            
        file.close()

# Add data to data_list and then update data.txt file
def add_data():
    last_line_number = []
    
    with open("data.txt", "r") as file:
        if os.stat("data.txt").st_size != 0:
            last_line_number = re.search("\d+", file.readlines()[-1])
        else:
            last_line_number.append(0)

    inp = input("Data to add: ")
    data_list.append(str((int(last_line_number[0]) + 1)) + ". " + inp + "\n")
    insert_data_into_file()
    print(str((int(last_line_number[0]) + 1)) + ". " + inp + ", has been added.")

# Display data in console
def display_data():
    for item in data_list:
        print(item.replace("\n", ""))

# Delete an item in data_list and update data.txt
def delete_data_item():
    inp = input("Type the number of the entry to delete: ")
    if os.stat("data.txt").st_size != 0:
        if inp != "0":
            item = data_list[int(inp) - 1]
            data_list.remove(item)
            insert_data_into_file()
            print(item.replace('\n', '') + ", has been removed.")
            count() # Reorder the data_list and data.txt to go from 1, 2, 3, etc...
        else:
            return print("0 cannot be removed since no entry can be 0.")
    else:
        return print("File \"data.txt\" is empty!")

exit_menu_loop = False

load_data_into_list()

while not exit_menu_loop:
    print("----------------------------")
    print("------------Menu------------")
    print("1. Display Data")
    print("2. Add Data")
    print("3. Delete Data Item")
    print("0. Exit Program")
    print("----------------------------")
    print("----------------------------")
    
    inp = input(">> ")
    
    if(re.search("0", inp)):
        exit_menu_loop = True
    elif(re.search("1", inp)):
        display_data()
    elif(re.search("2", inp)):
        add_data()
    elif(re.search("3", inp)):
        delete_data_item()
        