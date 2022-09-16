from mongoengine import *

connect(host='mongodb://localhost:27017/address_book')


class User(Document):
    login = StringField(max_length=50, required=True, unique=True)
    password = StringField(max_length=50, required=True)


class Person(Document):
    fullname = StringField(max_length=50, required=True)
    email = StringField(required=True)
    phone = StringField(required=True)


class Notice(Document):
    text = StringField(max_length=50, required=True)
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Person, reverse_delete_rule=CASCADE)
