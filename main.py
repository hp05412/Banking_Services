"""
@ Hitesh S Pandey

A Banking system which allows the user to interect with system and provides some services.
This prograame has been made from the scratch .
"""

import pickle
import os
import pathlib


class BankAccount:
    account_number = 0
    account_holder_name = ''
    account_balance = 0
    account_type = ''

    def create_account(self):
        self.account_number = int(input("Enter the account number: "))
        self.account_holder_name = input("Enter the account holder name: ")
        self.account_type = input("Enter the type of account [Current/Savings]: ")
        self.account_balance = int(input("Enter the initial amount (>= 1000 for Saving and >= 5000 for current): "))
        print("\n\n\nAccount Created")

    def show_account(self):
        print("Account Number: ", self.account_number)
        print("Account Holder Name: ", self.account_holder_name)
        print("Type of Account:", self.account_type)
        print("Balance: ", self.account_balance)

    def modify_account(self):
        print("Account Number: ", self.account_number)
        self.account_holder_name = input("Modify Account Holder Name: ")
        self.account_type = input("Modify type of Account: ")
        self.account_balance = int(input("Modify Balance: "))

    def deposit_amount(self, amount):
        self.account_balance += amount

    def withdraw_amount(self, amount):
        self.account_balance -= amount

    def report(self):
        print(self.account_number, " ", self.account_holder_name, " ", self.account_type, " ", self.account_balance)

    def get_account_number(self):
        return self.account_number

    def get_account_holder_name(self):
        return self.account_holder_name

    def get_account_type(self):
        return self.account_type

    def get_balance(self):
        return self.account_balance


def create_account():
    account = BankAccount()
    account.create_account()
    write_account_data(account)


def display_all_accounts():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        account_list = pickle.load(infile)
        for account in account_list:
            print(account.account_number, " ", account.account_holder_name, " ", account.account_type, " ",
                  account.account_balance)
        infile.close()
    else:
        print("No records to display")


def display_account_balance(account_number):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        account_list = pickle.load(infile)
        infile.close()
        found = False
        for account in account_list:
            if account.account_number == account_number:
                print("Your account Balance is = ", account.account_balance)
                found = True
    else:
        print("No records to Search")
    if not found:
        print("No existing record with this number")


def deposit_or_withdraw(account_number, transaction_type):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        account_list = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for account in account_list:
            if account.account_number == account_number:
                if transaction_type == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    account.deposit_amount(amount)
                    print("Your account is updated")
                elif transaction_type == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= account.account_balance:
                        account.withdraw_amount(amount)
                        print("Amount withdrawn Successfully ")
                    else:
                        print("You cannot withdraw a larger amount")

    else:
        print("No records to Search")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(account_list, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def close_account(account_number):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        old_account_list = pickle.load(infile)
        infile.close()
        new_account_list = []
        for account in old_account_list:
            if account.account_number != account_number:
                new_account_list.append(account)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(new_account_list, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print("Account has been deleted")


def modify_account_details(account_number):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        old_account_list = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for account in old_account_list:
            if account.account_number == account_number:
                account.account_holder_name = input("Enter the account holder name : ")
                account.account_type = input("Enter the account Type : ")
                account.account_balance = int(input("Enter the Amount : "))
                print("Account Modified Successfully")

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(old_account_list, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def write_account_data(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        old_account_list = pickle.load(infile)
        old_account_list.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        old_account_list = [account]
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(old_account_list, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


# Start of the program
choice = ''
account_num = 0

while choice != '8':
    print("\tMENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    choice = input()

    if choice == '1':
        create_account()
    elif choice == '2':
        account_num = int(input("\tEnter The account No. : "))
        deposit_or_withdraw(account_num, 1)
    elif choice == '3':
        account_num = int(input("\tEnter The account No. : "))
        deposit_or_withdraw(account_num, 2)
    elif choice == '4':
        account_num = int(input("\tEnter The account No. : "))
        display_account_balance(account_num)
    elif choice == '5':
        display_all_accounts();
    elif choice == '6':
        account_num = int(input("\tEnter The account No. : "))
        close_account(account_num)
        print("Account has been deleted")
    elif choice == '7':
        account_num = int(input("\tEnter The account No. : "))
        modify_account_details(account_num)
    elif choice == '8':
        print("\tThanks for using bank management system")
        break
    else:
        print("Invalid choice")

    choice = input("Enter your choice : ")
