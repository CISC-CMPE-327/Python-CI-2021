from qbay import *
from qbay.cli import login_page, regsiter_page


def main():
    while True:
        selection = input(
            'Welcome. Please type 1 to login. '
            'Or type 2 register. Or type 3 to exit')
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
        elif selection == '3':
            break


if __name__ == '__main__':
    main()
