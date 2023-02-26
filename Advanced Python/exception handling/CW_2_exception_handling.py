
import pandas as pd


costumes_dict = {'Fire man': 89, 'Police man': 105, 'Kohen gadol': 125, 'Kallah': 99, 'Mask': 15, 'Baker': 65}
order_list = []
print ('''Welcome to our "Masquerade"!!! Happy Purim!!! We sell Purim items!
Here are some options, Have fun choosing your costume:''')
for costume in costumes_dict.keys():
    print (costume)


def costume_order():    
    order = input('What costume would you like to purchse?')
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
            
            if confirmation.lower() == 'yes':
                order_list.append([order, costumes_dict[order], quantity])

            elif confirmation.lower() == 'no':
                costume_order()

            else:
                print('Invalid answer!')            
                

        except ValueError:
            print ('Invalid quantity!')

    except KeyError:
        print (f"We don't sell {order}.")   
   
    another_order = input('Would you like to purchase another item? Please enter yes or no.')

    if another_order == 'yes':
        costume_order()
    elif another_order == 'no':
        if len(order_list) < 1:
            print ("You are leaving our store without any purchases. Thank you and looking forward to seeing you again.")
        else:
            print ("Your bill is:")
            order_bill = pd.DataFrame(order_list, columns = ['Item', 'Price', 'Quantity'])
            order_bill['Item Total'] = order_bill['Quantity'] * order_bill['Price']
            print (order_bill)
            total = order_bill['Item Total'].sum()
            print (f"The total is: {total}.")
    else:
        costume_order()        
        
costume_order()

