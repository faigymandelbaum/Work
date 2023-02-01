from random import randint
from hashlib import sha256

def generate_pin(pin_length=3):
    if pin_length == 3:
        return sha256(bytes(randint(100, 999))).hexdigest()
    elif pin_length == 4:
        return sha256(bytes(randint(1000, 9999))).hexdigest()
    elif pin_length == 5:
        return sha256(bytes(randint(10000, 99999))).hexdigest()
    elif pin_length == 6:
        return sha256(bytes(randint(100000, 999999))).hexdigest()
    return ValueError('Pin length must be 3, 4, 5 or 6')


# Pin length can be between 3 and 6
pin = generate_pin(4)
with open('pin.txt', 'w') as f:
    f.write(str(pin))