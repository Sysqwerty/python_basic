class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id:int):
        for contact in self.contacts:
            if contact.get("id") == id:
                return contact
        return None

con = Contacts()
con.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
con.add_contacts("Mike Richards", "(698) 801-9856", "mike@utquamvel.net", True)
con.add_contacts('Wylie Pope', '(692) 802-2949', 'est@utquamvel.net', False)
con.add_contacts('Cyrus Jackson', '(501) 472-5218', 'nibh@semsempererat.com', False)
print(con.list_contacts())

print(con.get_contact_by_id(2))