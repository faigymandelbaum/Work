from random import randint

def generate_pin(pin_length=3):
    if pin_length == 3:
        return hash(bytes(randint(100, 999)))
    elif pin_length == 4:
        return hash(bytes(randint(1000, 9999)))
    elif pin_length == 5:
        return hash(bytes(randint(10000, 99999)))
    elif pin_length == 6:
        return hash(bytes(randint(100000, 999999)))
    return ValueError('Pin length must be 3, 4, 5 or 6')


# Pin length can be between 3 and 6
# pin = generate_pin(3)
pin = hash(bytes(567))
print('pin:', pin)