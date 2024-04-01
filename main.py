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
        if language in ['e', 'E', 'у', 'У']:
            return 'e'
        elif language in ['r', 'R', 'к', 'К']:
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
            x = alpha.index(symbol.lower())
            y = (x + shift) % (len(alpha))
            if upper_case == 0:
                return alpha[y]
            else:
                return  alpha[y].upper()

    else:
        return symbol


# Setting up the program
direct = encryption_or_decryption()
lang = english_or_russian()
sh = set_shift()

# Start the program
print('Enter the text:')
in_text = input()
# in_text = 'Умом Россию не понять'
out_text = ''
for sym in in_text:
    out_text += convert(sym, direct, lang, sh)
print(out_text)


