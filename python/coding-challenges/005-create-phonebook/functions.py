def menu():
    print("1. Find Phone Number")
    print("2. Insert a Phone Number")
    print("3. Delete a person from the phonebook")
    print("4. Terminate")
    print()

def insert_num():
    phone_dict = {}
    name = input("Insert name of the person: ")
    phone = input("Insert phone number of the person: ")
    if not phone.isdecimal:
        print ("Invalid input format, cancelling operation ...")
    else:
        
        phone_dict.update(name, phone)
        print ("Phone number of", name, "is inserted into the phonebook")
        return phone_dict 
    

    
   