from src.models import User, Person, Notice


def get_user(login) -> User:
    user = User.objects(login=login)
    return user[0]


def create_contact(fullname, email, phone):
    Person(fullname=fullname, email=email, phone=phone).save()


def update_contact(_id, fullname, email, phone):
    contact = Person.objects(id=_id)
    contact.update(fullname=fullname, email=email, phone=phone)
    return contact


def get_all_contacts():
    persons = Person.objects({})
    return persons


def search_contacts(fullname):
    contact = Person.objects(fullname=fullname)
    return contact[0]


def remove_contact(_id) -> int:
    contact = Person.objects(id=_id)
    contact.delete()


def add_notice(_id, description):
    contact = Person.objects(id=_id)
    Notice(text=description, tags=['web', 'life'], author=contact[0]).save()


def remove_notice(_id) -> int:
    notice = Notice.objects(id=_id)
    notice.delete()


def list_notice(_id):
    contact = Person.objects(id=_id)
    notices = Notice.objects(author=contact[0])
    return notices


