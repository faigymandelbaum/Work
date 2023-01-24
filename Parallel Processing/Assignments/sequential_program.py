import multiprocessing

class Mastercard:

    def __init__(self, name, id):
        self.customer_name = name
        self.customer_id = id

    def withdraw(customer_id, vendor, charge):
        print( "{} has charged customer ID: {} ${}.".format (vendor, customer_id, charge) )


withdrawl1 =  multiprocessing.Process(target = Mastercard.withdraw, args = ['JG1234', 'Shefa Birkat Hashem', 1500]) 
withdrawl2 =  multiprocessing.Process(target = Mastercard.withdraw, args = ['JG1234', 'Plumbing Service', 3200]) 
withdrawl3 =  multiprocessing.Process(target = Mastercard.withdraw, args = ['JG1234', 'Shaarei Revacha', 15.9]) 
withdrawl4 =  multiprocessing.Process(target = Mastercard.withdraw, args = ['JG1234', 'Einit', 650]) 



if __name__ == '__main__':
    withdrawl1.start()
    withdrawl2.start()
    withdrawl3.start()
    withdrawl4.start()

    withdrawl1.join()
    withdrawl2.join()
    withdrawl3.join()
    withdrawl4.join()

import multiprocessing

def multiply_number(number, multiplied):
    multiplied_number = number * 2
    multiplied.value = multiplied_number
    return

shared_val = multiprocessing.Value('i')

test = multiprocessing.Process(target=multiply_number, args=[12, shared_val])
if __name__ == '__main__':
    test.start()
    print(shared_val.value)

