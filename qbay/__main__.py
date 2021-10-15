from qbay import *
from qbay.cli import login_page, regsiter_page


def main():
    while True:
        selection = input(
            'Welcome. Please type 1 to login. Or type 2 register.')
        selection = selection.strip()
        if selection == '1':
            user = login_page()
            if user:
                print(f'welcome {user.username}')
                break
            else:
                print('login failed')
        elif selection == '2':
            regsiter_page()


if __name__ == '__main__':
    main()
