'''
Program toDoList.py
1/22/2024

Command Line app that lets the user select from a menu of five choices.
1. Add a task
2. View Task
3. Mark tasks as completed
4. Remove tasks from the list
5. Quit application
'''
# Empty global toDo array. The list constantly gets updated as user navigates the program
toDo = []
completed = []

# Definition of menu() function. Contains 5 options for user to select from
def menu():
    print("\nMain Menu")
    print("1 - Add a task")
    print("2 - View a task")
    print("3 - Mark task completed")
    print("4 - Remove a task")
    print("5 - Quit")
    choice = input("Please enter digit choice HERE: ")
    # While loop to let user input a digit
    while True:
        # If user inputs 1, call the create() function
        if choice == "1":
            create()
        # If user inputs 2, call the view() function
        elif choice == "2":
            view()
        # If user inputs 3, call the completed() function
        elif choice == "3":
            markCompleted()
        # If user inputs 4, call the remove() function
        elif choice == "4":
            remove()
        # If user inputs 5, print goodbye message and close the program
        elif choice == "5":
            print("Have a good day!")
            exit()
        # Else statement to stop user from entering invalid choices
        else:
            choice = input("Please enter a valid choice: \n")

# Definition of create() function. Lets user input tasks
def create():
    # While loop runs so user can continue to add tasks uninterrupted
    while True:
        addTask = input("Add task: ")
        # If user clicks enter, break loop
        if addTask == "":
            break
        # addTask variable appends onto the current toDo array
        else:
            toDo.append(addTask.upper())
    # Once while loop is broken, call the menu to let user choose new input
    menu()
    # Returns and updates the global toDo variable
    return toDo

# Definition of view() function
def view():
    while True:
        taskChoice = input("\n1 = View current To Do List\n2 = View completed Tasks\nPlease type 1 or 2: ")
        if taskChoice == "1":
            print("\nThis is your current To Do List")
            # For loop to display toDo list on individual lines
            for x in toDo:
                print(x)
            break
        elif taskChoice == "2":
            if len(completed) == 0:
                print("\nYour completed list is currently empty.")
                print("Returning to main menu...")
                break
            else:
                print("\nThese are your completed tasks:")
                for y in completed:
                    print(y)
                clear = input("\nWould you like to clear the list? Please type YES or NO.\nType your choice here: ")
                clear = clear.upper()
                while True:
                    if clear == "YES":
                        completed.clear()
                        print("\nYour completed list has been emptied.")
                        print("Returning to main menu...")
                        menu()
                    elif clear == "NO":
                        print("\nReturning to main menu...")
                        break
                    else:
                        print("\nInvalid input. Please type either YES or NO.")
                        clear = input("Type your choice here: ")
        else:
            print("Please enter a valid choice")
    # Once list is printed, call menu() function for user to select new input
    menu()
    return completed

def markCompleted():
    while True:
        mark = input("Please type the task you would like to mark as completed, or ENTER to quit: ")
        mark = mark.upper()
        if mark == "":
            print("Returning to main menu...")
            break
        elif mark not in toDo:
            print("Sorry, task not found")
            remove()
        else:
            list = toDo.index(mark.upper())
            toDo.pop(list)
            completed.append(mark)
            print("Task marked as completed...")
    # Call menu() function to have user select new input
    menu()
    return toDo, completed

# Definition of remove() function
def remove():
    while True:
        removeTasks = input("Please type the task you would like to remove, or ENTER to quit: ")
        removeTasks = removeTasks.upper()
        if removeTasks == "":
            print("Returning to main menu...")
            break
        elif removeTasks not in toDo:
            print("Sorry, task not found")
            remove()
        else:
            index = toDo.index(removeTasks.upper())
            toDo.pop(index)
            print("Task removed...")
    # Call menu() function to have user select new input
    menu()
    return toDo


menu()
toDo = create()
view(toDo)
toDo = remove()
toDo, completed = markCompleted()
