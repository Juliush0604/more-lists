"""
Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one
"""

shopping_list = []

#Uses while loop to continually check for new items
while True:
    #Asks what the user wants to do
    action = input("What would you like to do? \n 1. View shopping list \n 2. Add item to shopping list \n 3. Delete item in shopping list \n 4. Exit edit mode \n\n")
    #Displays list
    if action == "1":
        print(shopping_list, "\n")
    #Adds desired item to list
    elif action == "2":
        new_item = input("What would you like to add to your shopping list? \n\n")
        shopping_list.append(new_item)
    #Deletes desired item from list
    elif action == "3":
        deleted_item = input("What item would you like to delete? \n\n")
        #Checks if deleted item is actually on the list
        try:
            shopping_list.remove(deleted_item)
        except ValueError:
            print("Sorry, that is not an item on the list \n\n")
    #Exits edit mode
    elif action == "4":
        break
    #Stops any unknown action
    else:
        print("Sorry, that is not a valid action \n\n")

#Prints shopping list outside of edit mode
print("This is your current shopping list:", shopping_list)

