class PhoneBook:

    contacts = {}
    total_count = 0
    
    @staticmethod
    def welcome():
        print('welcome to PhoneBook Program ...')

    def menu(self):

        print("1.Create Contact")
        print("2.View Contacts")
        print("3.Update Contact")
        print("4.Delete Contact")
        print("5.Show Contact")
        print("6.Exit Phonebook")

        choice = int(input("Choose:"))
        return choice 
        
    def create_contact(self):
        name = input("Enter the name:")
        
        if name in self.contacts:
            print(f"{name} already exists.Please enter a different name")
        else:
            age = int(input("Enter the age:"))
            email = input("Enter the email:")
            phone_number = int(input("Enter the phone number:"))
            if len(str(phone_number)) != 11:
                    print("------------------------------")
                    print("Please enter a valid phone number")
                    print("------------------------------") 
            else:
                self.contacts[name]={
                    "Age" : age,
                    'Email' : email,
                    'Phone Number' : phone_number
            }
                print("------------------------------")
                print("Contact saved successufly......")
                print("------------------------------")
                self.total_count+=1
                
    def view_contacts(self):
        if self.total_count == 0:
            print("No Contact!!!")
        else:
            print('------------------------------')
            for name, information in self.contacts.items():
                print("Contact Name:", name)
                print("Contact Age:", information['Age'])
                print("Contact Email:", information['Email'])
                print("Contact Phone Number", information['Phone Number']) 
                print("Total Count:", self.total_count)
                print("------------------------------")
                

    def update_contact(self):
        name = input("Enter the name:").lower()
        if not name in self.contacts:
            print("------------------------------")
            print(f"Contact with the name of {name} does not exist")
            print("------------------------------")
        else:
            age = int(input("Enter the age:"))
            email = input("Enter the email:")
            phone_number = int(input("Enter the phone number:"))
            if len(str(phone_number)) > 11:
                        print("------------------------------")
                        print("Please enter a valid phone number....")
                        print("------------------------------")
            else:
                self.contacts[name]={
                "Age" : age,
                'Email' : email,
                'Phone Number' : phone_number
                }
                print("------------------------------")
                print("Updated successufly......")
                print("------------------------------")



    def delete_contact(self):
            name = input("Enter the name:").lower()
            if not name in self.contacts:
                print("------------------------------")
                print(f"Contact with the name of {name} does not exist")
                print("------------------------------")
            else:
                del self.contacts[name]
                print("------------------------------")
                print(f"Contact with the name of {name} deleted successfully......")
                print("------------------------------")


    def show_contact(self):
        name = input("Enter the name of the contact you want to been shown:").lower()
        if not name in self.contacts:
            print("------------------------------")
            print(f"Contact with the name of {name} does not exist")
            print("------------------------------")
        else:
            print('------------------------------')
            information = self.contacts[name]
            print("Contact Name:", name)
            print("Contact Age:", information['Age'])
            print("Contact Email:", information['Email'])
            print("Contact Phone Number", information['Phone Number']) 
            print("Total Count:", self.total_count)
            print("------------------------------")


p = PhoneBook()
PhoneBook.welcome()

while True:
 result = p.menu()
 if result == 1:
    p.create_contact()
 elif result == 2:
     p.view_contacts()
 elif result == 3:
     p.update_contact()
 elif result == 4:
     p.delete_contact()
 elif result == 5:
     p.show_contact()
 elif result == 6:
     break
 else:
     print("------------------------------")
     print("Please input valid number from above menu")
     print("------------------------------")
     
print("------------------------------")
print("Thank you for using our program")
print("------------------------------")
