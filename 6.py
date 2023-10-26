def decode(password):
    decoded_password = ''
    for char in password:
        if char > '2':
            new_char = str(int(char) - 3)
            decoded_password += new_char
        else:
            new_char = str(int(char) + 7)
            decoded_password += new_char
    return decoded_password
    return None