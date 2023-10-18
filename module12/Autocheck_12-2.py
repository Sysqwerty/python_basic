import json


filename = 'module12/Autocheck_12-2.json'

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
    with open(filename, 'w') as file:
        json.dump({"contacts": contacts}, file)


def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)["contacts"]


if __name__ == '__main__':
    write_contacts_to_file(filename, contacts)
    print(read_contacts_from_file(filename))


# import json

# some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
# file_name = 'data.json'

# with open(file_name, "w") as fh:
#     json.dump(some_data, fh)

# with open(file_name, "r") as fh:
#     unpacked = json.load(fh)

# unpacked is some_data  # False
# unpacked == some_data  # False

# unpacked['key'] == some_data['key']  # True
# unpacked['a'] == some_data['a']  # True
# unpacked['2'] == some_data[2]  # True
# unpacked['tuple'] == [5, 6]  # True
