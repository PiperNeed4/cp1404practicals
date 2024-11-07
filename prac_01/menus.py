"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

user_name = input("Enter name: ")
user_choice = input(f"(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()
while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {user_name}")
    elif user_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    user_choice = input(f"(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()
print("Finished")
