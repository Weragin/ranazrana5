from random import randint

def encrypt(path_input: str, path_output: str, first_shift: int):
    file_read = open(path_input, mode="r")
    file_write = open(path_output, mode="a")

    a = ord("a")
    file_write.write(chr(a + first_shift - 1))

    for character in file_read.readlines()[0]:
        if character.islower():
            file_write.write(chr((ord(character) - a + first_shift)%26 + a))

    for line in file_read.readlines()[1:]:
        shift = randint(1, 25)
        file_write.write(chr(a + shift - 1))
        for character in line:
            if character.islower():
                file_write.write(chr((ord(character) - a + shift)%26 + a))


def decrypt(path_input: str, path_output: str):
    file_read = open(path_input, mode="r")
    file_write = open(path_output, mode="a")
    a = ord("a")

    for line in file_read.readlines():
        shift = a - ord(line[0]) - 1
        
        for character in line[1:]:
            if character.islower():
                file_write.write(chr((ord(character) - a + shift)%26 + a))


def encrypt_decrypt(path_input, path_output, first_shift):
    if bool(first_shift):
        encrypt(path_input, path_output, first_shift)
    else:
        decrypt(path_input, path_output)

encrypt("ranazrana5/plain.txt", "ranazrana5/encrypted.txt", 2)
encrypt_decrypt("ranazrana5/encrypted.txt", "ranazrana5/decrypted.txt", 0)
