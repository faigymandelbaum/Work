
import pandas as pd
import logging
import os
import re


CURR_DIR = os.path.dirname(__file__)
LOG_FOLDER = CURR_DIR + '/logs'

logging.basicConfig(filename=LOG_FOLDER + '/my_costume_store_logs.txt',
                    filemode='a+',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

costumes_dict = {'Fire Man': 89, 'Police Man': 105,
                 'Kohen Gadol': 125, 'Kallah': 99, 'Mask': 15, 'Baker': 65}
order_list = []
customers_info = pd.DataFrame(columns=[
                              'first_name', 'last_name', 'phone_number', 'credit_card_number', 'total_purchases', 'amount_orders'])
print('''Welcome to our "Masquerade"!!! Happy Purim!!! We sell Purim items!
Here are some options, Have fun choosing your costume:''')
for costume in costumes_dict.keys():
    print(costume)

print('If you are signed up to our friend ship you can press f to escape. to sign up free, follow instructions:')


def costume_order():
    customer_phone_number = input('Please put in your phone number: ')
    if customer_phone_number not in customers_info['PhoneNumber']:
        print('You are not part of our customers yet, we areh happy for you to join.')
        f_name = input('What is your first name? ')
        l_name = input('Select your last name. ')
        credit_card_num = input(
            'Type in your credit card number so you can pay automatically.')
    order = input('What costume would you like to purchse?').title()
    try:
        try:
            print(f"The price for the {order} is: ${costumes_dict[order]}.")
        except:
            print(f"We don't sell {order}.")
            raise Exception
        quantity = input(f"How many {order}'s would you like ?")
        try:
            quantity = int(quantity)
            if quantity == 1:
                print(
                    f'''You chose {quantity} {order}. The price is: ${costumes_dict[order]}''')
            else:
                print(
                    f'''You chose {quantity} {order}'s. The total would be: ${costumes_dict[order]*quantity}''')

            confirmation = input(
                'Are you sure you want to place this order? Please enter yes or no.')

            if re.findall(r'y[es]?', confirmation.lower()):
                order_list.append([order, costumes_dict[order], quantity])
                logging.info(
                    f"{quantity} {order}'s were added to the shopping bag.")

            elif re.findall(r'n[o]?', confirmation.lower()):
                costume_order()

            else:
                raise Exception

        except:
            raise Exception



    another_order = input(
        'Would you like to purchase another item? Please enter yes or no.')

    if re.findall(r'y[es]?', another_order.lower()):
        costume_order()
    elif re.findall(r'n[o]?', another_order.lower()):
        if len(order_list) < 1:
            print("You are leaving our store without any purchases. Thank you and looking forward to seeing you again.")
        else:
            print("Your bill is:")
            order_bill = pd.DataFrame(
                order_list, columns=['Item', 'Price', 'Quantity'])
            order_bill['Item Total'] = order_bill['Quantity'] * \
                order_bill['Price']
            print(order_bill)
            total = order_bill['Item Total'].sum()
            print(f"The total is: ${total}.")
    else:
        costume_order()


costume_order()
