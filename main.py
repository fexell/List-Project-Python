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
            return print("File \"data.txt\" is empty...")
        
        file.close()
    
    return data_list

# Recount/reorder the list from 1, 2, 3, etc...
def count():
    if len(data_list) != 0:
        for item in range(len(data_list)):
            
            # Since there shouldn't be an item that is 0
            item += 1
            
            # m = match
            m = re.match("^(\d+\.\s+)(.*)", data_list[int(item) - 1])
            
            # s = search, and replace
            s = data_list[int(item) - 1].replace(m.groups()[0], str(item) + ". ")
            data_list[int(item) - 1] = s
            
            # Update data.txt file
            insert_data_into_file()
    else:
        return print("There is no data...")
        
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
            last_line_number = re.search("^(\d+)", file.readlines()[-1])
        else:
            last_line_number.append(0) # If data.txt file is empty append 0 to last_line_number and then increase it in append
            
        file.close()

    inp = input("Data to add: ")
    
    # Append the last_line_number + 1 to make the added item go to one step above the last number of the last item
    data_list.append(str((int(last_line_number[0]) + 1)) + ". " + inp + "\n")
    
    # Update data.txt file
    insert_data_into_file()
    
    #Let the user know that the item has been added to the data.txt file
    print(str((int(last_line_number[0]) + 1)) + ". " + inp + ", has been added.")

# Display data in console
def display_data():
    if len(data_list) != 0:
        for item in data_list:
            print(item.replace("\n", ""))
    else:
        return print("There is no data...")

# Delete an item in data_list and update data.txt
def delete_data_item():
    inp = input("Type the number of the entry to delete: ")
    
    # If input is not greater than the number of the last entry in data.txt file
    if not int(inp) > (len(data_list)):
        
        # If input is not 0
        if inp != "0":
            
            # If the data.txt is not empty
            if os.stat("data.txt").st_size != 0:
                item = data_list[int(inp) - 1]
                data_list.remove(item)
                
                # Update data.txt file
                insert_data_into_file()
                
                #Print and remove new-lines (\n), and let the user know which item was deleted
                print(item.replace('\n', '') + ", has been removed.")
                
                # Reorder the data_list and data.txt to go from 1, 2, 3, etc...
                count()
            else:
                return print("File \"data.txt\" is empty...")
        else:
            return print("Cannot choose 0 as an entry to delete...")
    else:
        return print("Number cannot be above " + str(len(data_list)) + "...")

# Swap two data items
def swap():
    
    # If the data_list list is not empty
    if len(data_list) != 0:
        inp_swap_1 = input("Enter the number of the entry to swap with: ")
        inp_swap_2 = input("Enter the second number of the entry to swap with: ")
        
        # First check if the input was the number 0
        if(inp_swap_1 != "0" and inp_swap_2 != "0"):
            
            # If the length of the inputs are not 0
            if len(inp_swap_1) != 0 or len(inp_swap_2) != 0:
                
                # If the inputs are the same number to swap with
                if inp_swap_1 != inp_swap_2:
                    to_swap_with_1 = data_list[int(inp_swap_1) - 1]
                    to_swap_with_2 = data_list[int(inp_swap_2) - 1]
                    data_list[int(inp_swap_1) - 1] = to_swap_with_2
                    data_list[int(inp_swap_2) - 1] = to_swap_with_1
                    
                    # Update data.txt file
                    insert_data_into_file()
                    
                    # Reorder the data_list and data.txt to go from 1, 2, 3, etc...
                    count()
                else:
                    return print("You cannot swap with the same number...")
            else:
                return print("You didn't enter a number for an entry to swap with...")
        else:
            return print("You cannot swap with number 0, since there can't be a number 0...")
    else:
        return print("There is no data...")
    
def edit():
    
    # If the data_list list is not empty
    if len(data_list) != 0:
        inp = int(input("Enter the number of the entry to edit: "))

        # If input is not greater than the number of the last entry in data.txt file
        if not int(inp) > (len(data_list)):
            
            # If input is not 0
            if inp != "0":
                to_edit = re.search("(\d+\.\s+)(.*)", data_list[inp - 1])
                inp_2 = input("Enter what to edit entry \"" + str(inp) + "\" with: ")
                data_list[inp - 1] = to_edit.groups()[0] + inp_2
                insert_data_into_file()
            else:
                return print("You cannot swap with number 0, since there can't be a number 0...")
        else:
            return print("Number cannot be above " + str(len(data_list)) + "...")
    else:
        return print("There is no data...")

# Variable to loop the menu
exit_menu_loop = False

# Load data into data_list list
load_data_into_list()

# Menu loop
while not exit_menu_loop:
    print("--------------------------------")
    print("--------------Menu--------------")
    print("1. Display Data")
    print("2. Add Data")
    print("3. Delete Data Item")
    print("4. Swap")
    print("5. Edit")
    print("0. Exit Program")
    print("--------------------------------")
    print("--------------------------------")
    
    inp = input(">> ")
    
    if(re.search("0", inp)):
        exit_menu_loop = True
    elif(re.search("1", inp)):
        display_data()
    elif(re.search("2", inp)):
        add_data()
    elif(re.search("3", inp)):
        delete_data_item()
    elif(re.search("4", inp)):
        swap()
    elif(re.search("5", inp)):
        edit()
        