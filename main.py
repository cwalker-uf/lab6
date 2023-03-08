# Lab 6 Group XX (Group 54 partner never responded to email)
# New partner: Luis Martinez (from Slack)
# Charleigh Walker

def encode_str(data_string):
    res = ""
    for char in data_string:
        if char.isdigit():
            digit = int(char) + 3
            if digit >= 10:
                digit -= 10
                res += str(digit)
            else:
                res += str(digit)
    return res


def decode(encoded_pw, data_string):
    print(f'The encoded password is {encoded_pw}, and the original password is {data_string}.\n')


def main():
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
        user_selection = int(input('Please enter an option: '))
        if user_selection == 1:
            data_string = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!\n')
            encoded_pw = encode_str(data_string)
            # Set a variable equal to the RETURN of function encode(); calls encode()
        elif user_selection == 2:
            decode(encoded_pw, data_string)  # calls decode()
        else:
            break


if __name__ == "__main__":
    main()


