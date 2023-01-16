

class Person:
    def __init__(self):
        self.full_name = None

def main():
    p = Person()
    p = setup_client(p)
    print(p.full_name)
    

def setup_client(person):
    person.full_name = input("Please input your full name:")
    return person
     
def say_hello(p):
    print("hello, " + p.full_name)
