from functions import *
book = {}
menu()
menu_choice = int(input("Select operation on Phonebook App (1/2/3) :"))
if menu_choice == 2:
    insert_num()
    book = insert_num()
print (book)

    