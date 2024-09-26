def main():
    minimum_length = 6
    user_password = get_password(minimum_length)
    print_asterisks(user_password)


def print_asterisks(user_password):
    print("*" * len(user_password))


def get_password(minimum_length):
    user_password = input("Enter password: ")
    while len(user_password) < minimum_length:
        print("Password is too short")
        user_password = input("Enter password: ")
    return user_password


main()
