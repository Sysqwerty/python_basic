import pickle

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Mister Rayen",
        "email": "rayen.x@gmail.com",
        "phone": "(992) 915-1234",
        "favorite": True,
    }
]


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    fileName = 'module12/Autocheck_12-1.bin'
    write_contacts_to_file(fileName, contacts)
    read_contacts_from_file(fileName)


# import pickle

# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# file_name = 'data.bin'

# with open(file_name, "wb") as fh:
#     pickle.dump(some_data, fh)

# with open(file_name, "rb") as fh:
#     unpacked = pickle.load(fh)

# print(unpacked == some_data)  # True
# print(unpacked is some_data)  # False
