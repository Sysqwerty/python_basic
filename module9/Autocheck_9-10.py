contacts = [
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


def get_favorites(contacts):
    return list(filter(lambda c: c.get("favorite"), contacts))


print(get_favorites(contacts))
