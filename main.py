def encryption_or_decryption():
    print('Select the direction:\n'
          '1 - encryption\n'
          '2 - decryption')
    direction = input()
    while direction not in ['1', '2']:
        print('Enter correct number:')
        direction = input()
    if direction == '1':
        return 1
    else:
        return 2


def english_or_russian():
    print('Select the language:\n'
          'e - English\n'
          'r - Russian')
    language = input()
    while True:
        if language in ['e', 'E', 'у', 'У']:
            return 'e'
        elif language in ['r', 'R', 'к', 'К']:
            return 'r'
        else:
            print('Enter correct value:')
            language = input()


# Setting up the program
print(encryption_or_decryption())
print(english_or_russian())
