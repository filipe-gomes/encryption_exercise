"""In this program we will encrypt and decrypt messages entered by the user"""

def get_mode():
    mode = input('Do you wish to encrypt or decrypt a message?\n')
    answers = ['encrypt', 'decrypt', 'e', 'd']
    if mode in answers:
        return mode
    else:
        print('Please enter one of the following as your answer: encrypt, decrypt, e or d.')

def get_message():
    message = input('Enter your message: ')
    return message

def get_translated_message(mode, message):
    key = 0
    if mode[0] == 'd':
        key = -1
    else:
        key = 1
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = get_mode()
message = get_message()

print('Your translated text is: ')
print(get_translated_message(mode, message))
