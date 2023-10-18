import csv


filename = 'module12/Autocheck_12-3.csv'

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


def write_contacts_to_file(filename: str, contacts: list):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=contacts[0].keys())
        writer.writeheader()
        writer.writerows(contacts)


def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        res = list(reader)
        for contact in res:
            contact['favorite'] = True if contact['favorite'] == 'True' else False
        print(res)
        return list(res)


if __name__ == '__main__':
    write_contacts_to_file(filename, contacts)
    print(read_contacts_from_file(filename))

# import csv

# with open('eggs.csv', 'w', newline='') as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# with open('eggs.csv', newline='') as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(', '.join(row))
