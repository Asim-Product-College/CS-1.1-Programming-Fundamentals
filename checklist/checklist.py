checklist = list()
# checklist.append("Hello")
# print(checklist)

def create(item):
    checklist.append(item)

def read(item):
    # if checklist[item] not in checklist:
    #     print("nodvsvuhsvcuscushfadisucashi")
    #     return False
    # if int(item) not in checklist:
    #     print("invalid index. Please choose a number between 0 and " + len(checklist)-1)
    print(checklist[int(item)])

# checklist = ['Hello', 'World']
# checklist[0] = "Cats"

def update(index, item):
    checklist[index] = item

# checklist = ['Hello', 'World']
# checklist.pop(1)

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(list_item)

def select(function_code):
    #Create item in checklist here
    if function_code == "C" or function_code == "c":
        item = input("What do you want to create? ")
        create(item)
    # Read item in checklist here
    elif function_code == "R" or function_code == "r":
        item = int(input("What index do you want to read? "))
        read(item)
    # Print all items here
    elif function_code == "P" or function_code == "p":
        list_all_items()
    # This is where we want to stop our loop
    elif function_code == "Q" or function_code == "q":
        return False
    else:
        #Catch all
        print("Unknown Option")
    return True

running = True

while running:
    selection = input("Press C to add to list, R to Read from list and P to display list: ")
    running = select(selection)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    
    destroy(1)
    print(read(0))

    list_all_items()

        # Call your new function with the appropriate value
    # select("C")
    #     # View the results
    # list_all_items()
    #     # Call function with new value
    # select("R")
    #     # View results
    # list_all_items()
        # Continue until all code is run
    # user_input("What is user input")