# It didn't work to do the multiprocessing on the create_account function, therefor it's hashed out.
import multiprocessing

class Vault:

    def __init__(self):
        self.accounts = {}
        self.preaddressed_envelope = multiprocessing.Value('f')
    

    def create_account(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name] += amount           
        else:
            self.accounts[account_name] = amount


    def get_money_from_accounts(self, account_names):
        total = 0
        if len(account_names) == len(self.accounts):
            total = sum(self.accounts.values())
        else:
            for account in account_names:
                total += int(self.accounts[account])
        with self.preaddressed_envelope.get_lock():
            self.preaddressed_envelope.value +=total


def main():

    my_vault = Vault()

    my_vault.create_account('50326', 325)
    my_vault.create_account('60258', 98.6)
    my_vault.create_account('50326', 4582)
    my_vault.create_account('54656', 1600)

    # account1 = multiprocessing.Process(target= my_vault.create_account, args=['50326', 325])
    # print ('done')
    # account2 = multiprocessing.Process(target= my_vault.create_account, args=['60258', 98.6])
    # print ('done')
    # account3 = multiprocessing.Process(target= my_vault.create_account, args=['50326', 4582])
    # print ('done')
    # account4 = multiprocessing.Process(target= my_vault.create_account, args=['54656', 1600])
    # print ('done')
    # print (my_vault.accounts)
    # print (my_vault.accounts_preaddressed_envelope.value)

    get_money1 = multiprocessing.Process(target=my_vault.get_money_from_accounts, args=[['54656', '50326']])
    get_money2 = multiprocessing.Process(target=my_vault.get_money_from_accounts, args=[['54656', '50326', '60258']])

    # account1.start()
    # account2.start()
    # account3.start()
    # account4.start()

    # account1.join()
    # account2.join()
    # account3.join()
    # account4.join()

    get_money1.start()
    get_money2.start()

    get_money1.join()
    get_money2.join()

    print(my_vault.preaddressed_envelope.value)

if __name__ == '__main__':
    main()    







