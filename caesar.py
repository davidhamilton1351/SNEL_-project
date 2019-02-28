def caesar_cipher():

    file = open("file6.txt", 'r')
    contents = file.read()
    new_char = ''
    for char in contents:
        n = ord(char)
        
        if n < 32:
            n = n + 95

        new_char += chr(n)

            
    return new_char


print(caesar_cipher())
