class ContactList:
    classmates = {}

    def __init__(self, name, number):
        self.name = name 
        self.number = number
 
    @classmethod
    def add_contact(cls, name, number):
        ContactList.classmates[name] = number 
    
    @classmethod
    def remove_contact(self, name):
        if name in the list, then remove from list
        
        return(self)

    def find_shared_contacts(self, name):
        return(self)

dude1 = ContactList.add_contact('Brian', 123456)
dude2 = ContactList.add_contact('Dan', 9876543)

print(ContactList.classmates)
#something = classmates.add_contact
