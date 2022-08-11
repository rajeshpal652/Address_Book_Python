class Contact():
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email
        self.return_list = self.addContact()

    def addContact(self):
        contact_list = [self.first_name, self.last_name, self.address,
                        self.city, self.state, self.zip, self.phone, self.email]
        return contact_list
if __name__ == "__main__":

    first_name = input("Enter the First Name : ")
    last_name = input("Enter the Last Name : ")
    address = input("Enter the Address : ")
    city = input("Enter the City : ")
    state = input("Enter the State : ")
    zip = input("Enter the Zip Code : ")
    phone = input("Enter the Phone Number : ")
    email = input("Enter the Email Id : ")
    contact = Contact(first_name, last_name, address, city, state, zip, phone, email)
    print(contact.return_list)