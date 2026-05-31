MENU = "(H)ello\n(G)oodnight\n(Q)uit"
name = input("Enter name: ")
print(MENU)
user_choice = input(">>> ").upper()
while user_choice != "Q":
    if user_choice == "H":
        print("Hello", name)
    elif user_choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    user_choice = input(">>> ").upper()
print("Finished")
