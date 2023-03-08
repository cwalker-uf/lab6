# Lab 6 Group XX (Group 54 partner never responded to email)
# New partner: Luis Martinez (from Slack)
# Charleigh Walker


def main():
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
        user_selection = int(input('Please enter an option: '))
        if user_selection == 1:
            user_pw = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            encoded_pw = encode(user_pw)  # Set a variable equal to the RETURN of function encode(); calls encode()
        elif user_selection == 2:
            decode(user_pw, encoded_pw)  # calls decode()
        else:
            break


def encode(user_pw):
    pw_arr = list(user_pw)  # turn the string into an array source: https://www.softwaretestinghelp.com/python/python-string-split/
    encoded_pw = ''  # initialize empty string to append
    for num in pw_arr:
        encoded_char = int(num) + 3  # index and add 3 to each digit
        if encoded_char >= 0 and encoded_char <= 9: # if the encoded character is between 0-9, append it to the string
            encoded_pw += str(encoded_char)
        elif encoded_char >= 10:  # checks if encoded_char exceeds 10
            remove_tens = encoded_char - 10  # remove 10s place and append it to the string
            encoded_pw += str(remove_tens)
    return encoded_pw

if __name__ == "__main__":
    main()

    # def decode(user_pw, encoded_pw):
    #     print(f'The encoded password is {encoded_pw}, and the original password is {user_pw}.')