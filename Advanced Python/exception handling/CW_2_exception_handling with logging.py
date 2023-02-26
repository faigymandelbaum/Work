
import pandas as pd
import logging
import traceback
import os
import re

CURR_DIR = os.path.dirname(__file__)
LOG_FOLDER = CURR_DIR + '/logs'

logging.basicConfig(filename=LOG_FOLDER + '/my_costume_store_logs.txt',
                    filemode='a+',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

costumes_dict = {'Fire Man': 89, 'Police Man': 105, 'Kohen Gadol': 125, 'Kallah': 99, 'Mask': 15, 'Baker': 65}
order_list = []
print ('''Welcome to our "Masquerade"!!! Happy Purim!!! We sell Purim items!
Here are some options, Have fun choosing your costume:''')

costume_list = [costume for costume in costumes_dict.keys()] 
for costume in costume_list:
    print (costume)


def costume_order():    
    order = input('What costume would you like to purchse?').title()
    try:
        print(f"The price for the {order} is: ${costumes_dict[order]}.")
        quantity = input(f"How many {order}'s would you like ?")
        try:
            quantity = int(quantity)
            if quantity == 1:
                print (f'''You chose {quantity} {order}. The price is: ${costumes_dict[order]}''')
            else:
                print (f'''You chose {quantity} {order}'s. The total would be: ${costumes_dict[order]*quantity}''') 

            confirmation = input ('Are you sure you want to place this order? Please enter yes or no.')
            
            if re.findall(r'y[es]?', confirmation.lower()):
                order_list.append([order, costumes_dict[order], quantity])
                print (f'{quantity} of the {order} costume successfully added to cart.')

            elif re.findall(r'n[o]?', confirmation.lower()):
                costume_order()

            else:
                print('Invalid answer!')            
                

        except ValueError:
            logging.error(traceback.format_exc())
            print ('Invalid quantity!')

    except KeyError:
        logging.error(traceback.format_exc())
        print (f"We don't sell {order}.") 


    another_order = input('Would you like to purchase another item? Please enter yes or no.')

    try:
        if re.findall(r'y[es]?', another_order.lower()):
            costume_order()
        elif re.findall(r'n[o]?', another_order.lower()):
            if len(order_list) < 1:
                print("You are leaving our store without any purchases. Thank you and looking forward to seeing you again.")
            else:
                print ("Your bill is:")
                order_bill = pd.DataFrame(order_list, columns = ['Item', 'Price', 'Quantity'])
                order_bill['Item Total'] = order_bill['Quantity'] * order_bill['Price']
                print (order_bill)
                total = order_bill['Item Total'].sum()
                print (f"The total is: {total}.")
                went_through = False
                cc_number = input ("To pay, enter your credit card number: ")
                while went_through == False:
                    #cc_number = input ("To pay, enter your credit card number: ")
                    if re.findall(r'\d{4}\s?\d{4}\s?\d{4}\s?\d{4}', cc_number):
                        print (f'${total} payed successfully.')
                        logging.info('Payment ran successfully.')
                        went_through = True
                    else:
                        cc_number = input("Please try again. To leave without paying enter e(xit): ")
                        if re.findall(r'e[xit]?', cc_number.lower()):
                            went_through = True
                            print ('Your order ws canceled.')
                        else:
                            went_through = False

            
        else:
            costume_order() 

    except Exception as e:
        print (e)               
        
costume_order()


