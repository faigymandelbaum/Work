import csv

class CreditCardStatement:
    
    # class attributes:

    user = 'user name'
    pswd = 'users password'
    bills = 'bill_information'

    def __init__(self, bill_information):
        self.__path = bill_information
        self.bills = []

    def open_txt_file(self):
        file = open(self.__path)
        csv_reader = csv.reader(file)
        self.bills = list(csv_reader)

    def split_date(self):
        for bill in self.bills:
            bill[2] = bill[2].split("\t")[0]

    def print_total(self):
        total = 0.0
        for bill in self.bills:
            total += float(bill[1])    
        return ('The total is: ${}.'.format(total)) 

    def bill_designing(self):
        print ('Your charges are:')
        description = ''
        for bill in self.bills:
            description += '\n' +"On " + bill[2] + ", " + "$" + bill[1] + " were spent at " + bill[0] + '.'
        return description          
            
            
    def __str__(self):   
        if self.bills == []:
            return 'Welcome to the bank account. The user is not recognized'
        else:
            return "Welcome to your private account!"

    

def main():
    my_bills = CreditCardStatement('C:/Users/Owner/Documents/Course/A Faigy Mandelbaum Work/OOP/Assignments/CreditCardStatement/credit_card_bill.txt')
    my_bills.open_txt_file()
    my_bills.split_date()
    print(my_bills)


if __name__ == "__main__":
    main()

anonymous_bills = CreditCardStatement ('C:/Users/Owner/Documents/Course/A Faigy Mandelbaum Work/OOP/Assignments/CreditCardStatement/credit_card_bill.txt')
print (anonymous_bills)   

