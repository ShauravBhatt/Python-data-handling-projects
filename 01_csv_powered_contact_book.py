"""  
 Challenge: CLI Contact Book (CSV-Powered)                                                   
                                                                                             
Create a terminal-based contact book tool that stores and manages contacts using a CSV file. 
                                                                                             
Your program should:                                                                         
1. Ask the user to choose one of the following options:                                      
   - Add a new contact                                                                       
   - View all contacts                                                                       
   - Search for a contact by name                                                            
   - Exit                                                                                    
2. Store contacts in a file called `contacts.csv` with columns:                              
   - Name                                                                                    
   - Phone                                                                                   
   - Email                                                                                   
3. If the file doesn't exist, create it automatically.                                       
4. Keep the interface clean and clear.                                                       
                                                                                             
Example:                                                                                     
Add Contact                                                                                  
View All Contacts                                                                            
Search Contact                                                                               
Exit                                                                                         

Bonus:                                                                                       
- Format the contact list in a table-like view                                               
- Allow partial match search                                                                 
- Prevent duplicate names from being added                                                   
"""                                                                                          

import csv
import os 

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME , "w" , newline="" , encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name" , "Phone" , "Email"])

def add_contact():
    name = input("\nEnter name: ").strip().lower()
    
    with open(FILENAME , "r" , encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for data in reader:
            if data["Name"] == name:
                print("\nContact already exists !!")
                return 

    phone = input("Enter phone number: ").strip()
    
    if not (phone.isdigit() and len(phone) == 10 and phone[0] in "6789"):
        print("Entered phone number is invalid !!")
        return

    email = input("Enter email: ").strip().lower()

    with open(FILENAME , "a" , encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name,phone,email])
        print("\nContact added successfully !!")

def view_contacts():
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if len(rows) < 1 :
            print("\nContact book is empty !!")
            return 

        print("\nYour contacts are: \n")
        for indx, row in enumerate(rows , start=1):
            print(f"{indx}.) {row["Name"].capitalize()}| {row["Phone"]} | {row["Email"]}")
        print()

def search_contact():
    name = input("\nEnter the name of contact: ").strip().lower()
    
    with open(FILENAME , "r" , encoding="utf-8") as f:
        reader = csv.DictReader(f)
        found = False 

        for data in reader:
            if data["Name"].lower() == name:
                print(f"\n{data['Name']} | {data['Phone']} | {data['Email']}")
                found = True 
                return

        if found == False:
            print("\nContact not found !!")

def delete_contact():
    name = input("\nEnter the name to delete contact: ").strip().lower()
    contacts = []

    with open(FILENAME,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        contacts = list(reader)
        fieldnames = reader.fieldnames

    update_contacts = [contact for contact in contacts if contact["Name"] != name]

    with open(FILENAME,"w",encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(update_contacts)

    print(f"\nContact with name '{name.capitalize()}' deleted successfully !!")

def main():

    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nChoose an option (1-5) : ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\nThanks for using our software")
            break
        else:
            print("\nInvalid choice of number")


if __name__ == "__main__":
    main()
