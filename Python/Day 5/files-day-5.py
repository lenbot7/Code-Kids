"""
Files R/W and Encryption
Lenny
Day 5
"""


def shift_creation(password):
    total = 0
    for char in password:
        total += ord(char)
    return total % 256


def encrypt_file(file, password):
    shift = shift_creation(password)
    with open(file, 'r') as f:
        content = f.read()
    encrypted = ''
    for char in content:
        encrypted += chr(ord(char) + shift)
    with open(file, 'w') as f:
        f.write(encrypted)


def decrypt_file(file, password):
    shift = shift_creation(password)
    with open(file, 'r') as f:
        content = f.read()
    decrypted = ''
    for char in content:
        decrypted += chr(ord(char) - shift)
    with open(file, 'w') as f:
        f.write(decrypted)


def main():
    file = input('Enter file name: ')
    password = input('Enter password: ')
    choice = input('Encrypt or Decrypt? (E/D): ')
    if choice.lower() == 'e':
        encrypt_file(file, password)
    else:
        decrypt_file(file, password)


if __name__ == '__main__':
    main()
