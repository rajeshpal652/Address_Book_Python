class Contact():
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone = phone
        self.__email = email
        self.returned_list = self.addContact()

    def setFirst_name(self,first_name):
        self.__first_name = first_name
    def getFirst_name(self):
        return self.__first_name
    def setLast_name(self,last_name):
        self.__last_name = last_name
    def getLast_name(self):
        return self.__last_name
    def setAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setCity(self,city):
        self.__city = city
    def getCity(self):
        return self.__city
    def setState(self,state):
        self.__stazip
    def getState(self):
        return self.__state
    def setZip(self,zip):
        self.__zip = zip
    def getZip(self):
        return self.__zip
    def setPhone(self,phone):
        self.__phone = phone
    def getPhone(self):
        return self.__phone
    def setEmail(self,email):
        self.__email = email
    def getEmail(self):
        return self.__email
    def addContact(self):
        contact_list = [self.getFirst_name(), self.getLast_name(), self.getAddress(),
                        self.getCity(), self.getState(), self.getZip(), self.getPhone(), self.getEmail()]
        return contact_list
    # def editContact(self, first_name, last_name, address, city, state, zip, phone, email):
    #     self.setFirst_name(first_name)
    #     self.setLast_name(last_name)
    #     self.setAddress(address)
    #     self.setCity(city)
    #     self.setState(state)
    #     self.setZip(zip)
    #     self.setPhone(phone)
    #     self.setEmail(email)


if __name__ == "__main__":
    condition = True
    contacts_list = []
    while condition == True:
        print("")
        print("<=========================Address Book Management System=========================>")
        choice = int(input("1. Enter 1 to add new Contact \n"
                           "2. Enter 2 to view all contacts \n"
                           "3. Enter 3 to edit Contact \n"
                           "4. Enter 4 to Delete Contact \n"
                           "5. Exit \n"))

        if(choice == 1):
            first_name = input("Enter the First Name : ")
            last_name = input("Enter the Last Name : ")
            address = input("Enter the Address : ")
            city = input("Enter the City : ")
            state = input("Enter the State : ")
            zip = input("Enter the Zip Code : ")
            phone = input("Enter the Phone Number : ")
            email = input("Enter the Email Id : ")
            contact = Contact(first_name, last_name, address, city, state, zip, phone, email)
            contacts_list.append(contact.returned_list)
            print(contacts_list[len(contacts_list)-1])

        elif (choice == 2):
            print(contacts_list)

        elif(choice == 3):
            first_name_check = input("Enter the First Name to Edit Contact: ")
            for contact_data in contacts_list:
                if(first_name_check in contact_data):
                    print("Contact Found : Enter the details to update")
                    first_name = input("Enter the First Name : ")
                    last_name = input("Enter the Last Name : ")
                    address = input("Enter the Address : ")
                    city = input("Enter the City : ")
                    state = input("Enter the State : ")
                    zip = input("Enter the Zip Code : ")
                    phone = input("Enter the Phone Number : ")
                    email = input("Enter the Email Id : ")
                    index = contacts_list.index(contact_data)
                    contacts_list[index] = [first_name, last_name, address, city, state, zip, phone, email]
                    print(contacts_list[index])
                else:
                    print("Contact not Found")
        elif (choice == 4):
            first_name_check = input("Enter the First Name to Edit Contact: ")
            for contact_data in contacts_list:
                if (first_name_check in contact_data):
                    contacts_list.remove(contact_data)
                    print("Contact deleted Successfully")
                else:
                    print("Contact not found")
        else:
            condition = False
