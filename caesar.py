#caesar.py

# Run a simple caesar cipher on the message
def encode_caesar(message, secret):
    offset = len(secret)
    offset %= 26
    return do_caesar(message, offset)

def decode_caesar(message, secret):
<<<<<<< HEAD
    offset = len(secret)
    offset %= 26
    offset = 26 - offset
    return do_caesar(message, offset)
=======
    return message #Real implementation in caesarfeat!
>>>>>>> 335ebd403d62bd8e5ec418742f5989d9080f3513

# Performs the caesar cipher operation
def do_caesar(message, offset):
    newmsg = ""
    for letter in message:
        if(letter.isupper()):
            number = ord(letter) + offset
            if(number >= (65+26)):
                number -= 26
            letter = chr(number)
        elif(letter.islower()):
            number = ord(letter) + offset
            if(number >= (97+26)):
                number -= 26
            letter = chr(number)
        newmsg += letter
    return newmsg