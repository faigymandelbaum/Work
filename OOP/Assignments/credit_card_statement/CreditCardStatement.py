import csv

class CreditCardStatement:
    
    # class attributes:

    user = 'user name'
    pswd = 'users password'
    bills = 'bill_information'

    def __init__(self, bill_information):
        self.path = bill_information

    def open_txt_file(self):
        file = open(self.path)
        csv_reader = csv.reader(file)
        self.bills = list(csv_reader)

    def split_date(self):
        for bill in self.bills:
            bill[2] = bill[2].split("\t")[0]
            
            
    def __str__(self):
        print ('Your charges are:')
        for bill in self.bills:
            description = "On " + bill[2] + ", " + "$" + bill[1] + " were spent at " + bill[0] + '.'
            print (description)
        total = 0.0
        for bill in self.bills:
            total += float(bill[1])    
        return ('The total is: ${}.'.format(total))   

def main():
    my_bills = CreditCardStatement('C:/Users/Owner/Documents/Course/A Faigy Mandelbaum Work/OOP/Assignments/CreditCardStatement/credit_card_bill.txt')
    my_bills.open_txt_file()
    my_bills.split_date()
    print(my_bills)


if __name__ == "__main__":
    main()