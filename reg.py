from src.models import User

if __name__ == '__main__':
    login = input('login: ')
    password = input('password: ')
    usr = User(login=login, password=password).save()