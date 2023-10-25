def encode(password: str) -> str:
    return ' '.join(str(int(num) + 3) for num in password)


def decode(password: str):
    # partner codes this
    password = list(password)
    decoded_password = []
    for num in password:
        new_num = int(num) - 3
        if new_num < 0:
            new_num += 10
        decoded_password.append(str(new_num))
    decoded_password = "".join(decoded_password)
    return decoded_password


def main():
    menu_option = None
    password = ""
    encoded_password = ""
    while menu_option != '3':
        menu_option = input("Please enter an option: ")
        # Jason edit: encode password (add 3 to each int in string)
        if menu_option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password=password)
            print("Your password has been encoded and stored!")
        elif menu_option == '2':
            pass
            # print(f"The encoded password is {encoded_password}, and the original password is {password}.")


if name == 'main':

    main()