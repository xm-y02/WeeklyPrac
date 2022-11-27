MIN_LENGTH = 8


def main():
    user_password = get_password()
    display_stars(user_password)


def display_stars(user_password):
    print('*' * len(user_password))


def get_password():
    user_password = input("Enter password: ")
    while len(user_password) < MIN_LENGTH:
        print("Invalid. Please enter at least 8 characters.")
        user_password = input("Enter password: ")
    return user_password


main()
