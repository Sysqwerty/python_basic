class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name: str, phone: str, email: str, favorite: bool):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        self.contacts.append(contact)
        Contacts.current_id += 1


con = Contacts()
con.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
print(con.list_contacts())
con.add_contacts("Mike Richards", "(698) 801-9856", "mike@utquamvel.net", True)
print(con.list_contacts())
con.add_contacts('Wylie Pope', '(692) 802-2949', 'est@utquamvel.net', False)
print(con.list_contacts())
con.add_contacts('Cyrus Jackson', '(501) 472-5218', 'nibh@semsempererat.com', False)
print(con.list_contacts())
