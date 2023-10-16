list_contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }, {
        "name": "Mile Bobler",
        "email": "mile.bobler@gmail.com",
        "phone": "(098) 123-4567",
        "favorite": True,
    }
]


# def get_emails(list_contacts):
#     res = list()

#     for i in map(lambda contact: contact.get("email"), list_contacts):
#         res.append(i)

#     return res

def get_emails(list_contacts):
    return list(map(lambda contact: contact.get("email"), list_contacts))


print(get_emails(list_contacts))
