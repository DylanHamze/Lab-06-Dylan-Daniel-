def decoder(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        old_number = str((int(digit) - 3) % 10)
        decoded_password += old_number
    return decoded_password
