from qbay.models import login, register


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def regsiter_page():
    email = input('Please input email:')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('password entered not the same')
    elif register('default name', email, password):
        print('registration succceeded')
    else:
        print('regisration failed.')
