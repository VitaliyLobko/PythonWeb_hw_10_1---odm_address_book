import argparse
import sys
from src.repository import get_user, create_contact, get_all_contacts, update_contact, remove_contact, search_contacts
from src.repository import add_notice, list_notice, remove_notice


parser = argparse.ArgumentParser(description='address book')
parser.add_argument('--action', help='Command: create, update, list, search, remove, add_notice')
parser.add_argument('--fullname')
parser.add_argument('--email')
parser.add_argument('--phone')
parser.add_argument('--login')
parser.add_argument('--id')
parser.add_argument('--description')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
fullname = my_arg.get('fullname')
email = my_arg.get('email')
phone = my_arg.get('phone')
login = my_arg.get('login')
_id = my_arg.get('id')
description = my_arg.get('description')


def main():
    match action:
        case 'create':
            create_contact(fullname=fullname, email=email, phone=phone)
        case 'list':
            persons = get_all_contacts()
            for t in persons:
                print(t.id, t.fullname, t.email, t.phone)
        case 'update':
            t = update_contact(_id=_id, fullname=fullname, email=email, phone=phone)
            print(t.id, t.fullname, t.email, t.phone)
        case 'remove':
            r = remove_contact(_id=_id,)
            print(f'Result: {bool(r)}')
        case 'search':
            t = search_contacts(fullname=fullname)
            print(t.id, t.fullname, t.email, t.phone)
        case 'add_notice':
            add_notice(_id=_id, description=description)
        case 'list_notice':
            r = list_notice(_id=_id)
            for t in r:
                print(f'id = {t.id} | Name: {t.author.fullname} |  text: {t.text}')
        case 'remove_notice':
            r = remove_notice(_id=_id)

login='lucky'
if __name__ == '__main__':
    user = get_user(login)
    password = input('password: ')
    if password == user.password:
        main()
    else:
        print('Wrong password!')
        sys.exit()

# py main.py --action create --fullname Vasya --phone 1234567890 --email test@test.com --login lucky
# py main.py --action update --id 632406d9db6e6004fcef3cc5 --fullname Vasya11 --phone 1234567890 --email test@test.com --login lucky
# py main.py --action search --fullname Vasya --login lucky
# py main.py --action list --login lucky
# py main.py --action remove --id 632406d9db6e6004fcef3cc5 --login lucky


# py main.py --action add_notice --id 63240781a4c6a7fc329207f2 --description 'sdfsdfsdf sdf ssdf sdf sd' --login lucky
# py main.py --action remove_notice --id 63240ca9c9893d2fc2837173 --login lucky
# py main.py --action list_notice --id 63240781a4c6a7fc329207f2 --login lucky
