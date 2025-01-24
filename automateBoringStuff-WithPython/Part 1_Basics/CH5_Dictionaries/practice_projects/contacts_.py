contacts = {
    # Default values
        'Support': {'name':'Support', 'phone': '091', 'country': 'Iran'},
}

def add_contact(name, phone, country):
    contacts[name] = {'phone': phone, 'country': country}

def search_contact(name):
    if name in contacts:
        for key, value in contacts[name].items():
            print(key + ': ' + value)
    else:
        print('Contact not found')

def show_all_contacts():
    for name, contact in contacts.items():
        print(name)
        for key, value in contact.items():
            print('\t' + key + ': ' + value)

def delete_contact(name):
    if name in contacts:
        choise = input('Are you sure you want to delete ' + name + '? (y/n) ')
        if choise == 'y':
            del contacts[name]
            print('Contact deleted')
        else:
            print('Contact not deleted')
    else:
        print('Contact not found')

def main():
    while True:
        print(('Contact Support'
               ' number: ') + contacts[ 'Support'][ 'phone'])
        print('1. Add contact')
        print('2. Search contact')
        print('3. Show all contacts')
        print('4. Delete contact')
        print('5. Exit')
        choise = input('Enter your choise: ')
        if choise == '1':
            name = input('Enter contact name: ')
            phone = input('Enter contact phone: ')
            country = input('Enter contact country: ')
            add_contact(name, phone, country)

        elif choise == '2':
            name = input('Enter contact name: ')
            search_contact(name)

        elif choise == '3':
            show_all_contacts()

        elif choise == '4':
            name = input('Enter contact name: ')
            delete_contact(name)

        elif choise == '5':
            exit()

if __name__ == '__main__':
    main()