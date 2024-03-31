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


print(encryption_or_decryption())
