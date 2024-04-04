english_letters = 'abcdefghijklmnopqrstuvwxyz'
russian_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


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
        if language.lower() == 'e':
            return 'e'
        elif language.lower() == 'r':
            return 'r'
        else:
            print('Enter correct value:')
            language = input()


def set_shift():
    print('Set the shift:')
    shift = input()
    while not shift.isdigit():
        print('Enter correct value:')
        shift = input()
    return int(shift)


def convert(symbol, direction, language, shift):
    if language == 'e':
        alpha = english_letters
    else:
        alpha = russian_letters

    if symbol.lower() in alpha:
        if symbol == symbol.upper():
            upper_case = 1
        else:
            upper_case = 0

        if direction == 1:
            decr_index = alpha.index(symbol.lower())
            encr_index = (decr_index + shift) % (len(alpha))
            if upper_case == 0:
                return alpha[encr_index]
            else:
                return alpha[encr_index].upper()
        elif direction == 2:
            encr_index = alpha.index(symbol.lower())
            decr_index = (encr_index - shift) % (len(alpha))
            if upper_case == 0:
                return alpha[decr_index]
            else:
                return alpha[decr_index].upper()
    else:
        return symbol


# Setting up the program
direct = encryption_or_decryption()
lang = english_or_russian()
sh = set_shift()

# Start the program
print('Enter the text:')
in_text = input()
out_text = ''
for sym in in_text:
    out_text += convert(sym, direct, lang, sh)
print(out_text)
